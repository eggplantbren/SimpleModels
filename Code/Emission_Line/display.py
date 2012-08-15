import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('../emission_line_data.txt')
x = data[:,0]
sample = np.atleast_2d(np.loadtxt('posterior_sample.txt'))

plt.ion()

flux = np.empty(sample.shape[0])
for i in xrange(0, sample.shape[0]):
	mock = sample[i, 0]*np.exp(-0.5*((x - sample[i, 1])/sample[i, 2])**2)
	flux[i] = sum(mock)

	plt.hold(False)
	plt.plot(x, mock, 'k')
	plt.hold(True)
	plt.errorbar(x, data[:,1], yerr=data[:,2], fmt='ro')
	plt.title(str(i+1))
	plt.draw()

plt.ioff()
plt.show()

plt.hist(flux, 30)
plt.show()

