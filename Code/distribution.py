"""
Code for fitting a simple 1-D PDF to a complex one, by maximum entropy
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# A Pareto (power-law) distribution
class Simple:
	"""
	Constructor: takes a minimum value cutoff
	and a slope parameter
	"""
	def __init__(self, xMin, alpha):
		assert xMin > 0 and alpha > 0
		self.xMin, self.alpha = xMin, alpha
	"""
	Evaluate the probability density given a numpy
	array of x-points
	"""
	def pdf(self, x, normalise=False):
		p = np.zeros(x.shape)
		good = np.nonzero(x > self.xMin)[0]
		p[good] = self.alpha*self.xMin**self.alpha/x**(self.alpha + 1)
		if normalise:
			p = p/np.trapz(p, x=x)
		return p

# A mixture of N exponentials
class Complex:
	"""
	Constructor: takes a numpy array of 
	means and weights
	"""
	def __init__(self, xMin, means, weights):
		assert weights.size == means.size
		assert xMin > 0
		weights = weights/weights.sum()
		self.xMin, self.means, self.weights = xMin, means, weights
		
	def pdf(self, x, normalise=False):
		p = np.zeros(x.shape)
		good = np.nonzero(x > self.xMin)[0]
		for i in xrange(0, self.weights.size):
			p[good] += self.weights[i]/(self.means[i])*np.exp(-(x[good] - self.xMin)/self.means[i])
		if normalise:
			p = p/np.trapz(p, x=x)
		return p

def entropy(simple, complicated, x):
	p_simple = simple.pdf(x, normalise=True)
	p_complex = complicated.pdf(x, normalise=True)
	H = -np.trapz(x, p_complex*np.log(p_complex/(p_simple + 1E-300) + 1E-300))
	return H

complicated = Complex(1.0, np.array([1.0, 3.0]), np.array([0.5, 0.5]))
x = np.linspace(1.0, 100.0, 10001)

def minimiseMe(params):
	if params < 0:
		return 1E300
	simple = Simple(1.0, params)
	return -entropy(simple, complicated, x)

# Executable code
if __name__ == '__main__':

	params = 1.0
	params = scipy.optimize.fmin(minimiseMe, params)
	simple = Simple(1.0, params)	

	plt.plot(x, complicated.pdf(x, normalise=True), 'b')
	plt.plot(x, simple.pdf(x, normalise=True), 'r')
	plt.show()

