"""
Code for fitting a simple 1-D PDF to a complex one, by maximum entropy
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# A normal distribution
class Simple:
	def __init__(self, mu=0., log_sig=0.):
		"""
		Constructor: takes a mean and a log-standard deviation
		"""
		self.mu, self.sig = mu, np.exp(log_sig)

	def pdf(self, x):
		"""
		Evaluate the probability density given a numpy
		array of x-points
		"""
		p = 1./self.sig/np.sqrt(2*np.pi)\
			*np.exp(-0.5*((x - self.mu)/self.sig)**2)
		return p

# A mixture of N concentric gaussians
class Complex:
	def __init__(self, mu=0., sig=np.array([1.,1.]),\
			weights=np.array([0.5, 0.5])):
		"""
		Constructor: takes a mean, a tuple of sigmas
		and a tuple of not-necessarily normalised weights
		"""
		assert sig.size == weights.size
		assert np.all(weights >= 0.) and np.all(sig > 0.)
		self.N = sig.size
		self.mu, self.sig, self.weights = mu, sig, weights/weights.sum()

	def pdf(self, x):
		p = np.zeros(x.shape)
		for i in xrange(0, self.N):
			p += self.weights[i]/self.sig[i]/np.sqrt(2*np.pi)\
				*np.exp(-0.5*((x - self.mu)/self.sig[i])**2)
		return p

	def generate_data(self):
		pass

def utility(simple, complicated, x):
	U = np.trapz(complicated.pdf(x)*np.log(simple.pdf(x) + 1E-300), x=x)
	return U

# Executable code
if __name__ == '__main__':
	x = np.linspace(-10., 10., 1001)
	complicated = Complex(mu=0., sig=np.array([0.3, 1., 3.]),\
				weights=np.array([0.5, 0.5, 0.5]))

	def minimiseMe(params):
		simple = Simple(mu=params[0], log_sig=params[1])
		return -utility(simple, complicated, x)

	params = np.array([0., 0.])
	params = scipy.optimize.fmin(minimiseMe, params)
	simple = Simple(mu=params[0], log_sig=params[1])	

	plt.plot(x, complicated.pdf(x), 'b')
	plt.plot(x, simple.pdf(x), 'r')
	plt.show()

