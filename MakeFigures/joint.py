from pylab import *

"""
Plot an illustrative joint prior implied by a complex
model, and then the same thing implied by a simple model.
"""

x = linspace(-10, 10, 201)
y = linspace(-10, 10, 201)
[x, y] = meshgrid(x, y)
y = y[::-1, :]

px = exp(-0.5*x**2)
for i in xrange(0, x.shape[1]):
	px[i, :] /= px[i, :].sum() 

pyx  = x.copy()
for i in xrange(0, x.shape[1]):
	pyx[:,i] = exp(-0.5*(y[:,i] - x[:,i])**2)
	pyx[:,i] /= pyx[:,i].sum()

joint = px*pyx
pxy = joint.copy()
for i in xrange(0, y.shape[0]):
	pxy[i, :] = joint[i, :]/joint[i, :].sum()

subplot(2,3,1)
imshow(joint, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(\\theta, x)$')

subplot(2,3,2)
imshow(pyx, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(x|\\theta)$')

subplot(2,3,3)
imshow(pxy, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(\\theta|x)$')

px = exp(-0.5*x**2/3**2)
for i in xrange(0, x.shape[1]):
	px[i, :] /= px[i, :].sum() 

pyx  = x.copy()
for i in xrange(0, x.shape[1]):
	pyx[:,i] = exp(-0.5*(y[:,i] - x[:,i])**2/0.3**2)
	pyx[:,i] /= pyx[:,i].sum()

joint = px*pyx
pxy = joint.copy()
for i in xrange(0, y.shape[0]):
	pxy[i, :] = joint[i, :]/joint[i, :].sum()

subplot(2,3,4)
imshow(joint, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(\\theta, x)$')

subplot(2,3,5)
imshow(pyx, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(x|\\theta)$')

subplot(2,3,6)
imshow(pxy, extent=[-10, 10, -10, 10])
xlabel('$\\theta$')
ylabel('$x$')
title('$p(\\theta|x)$')


show()


