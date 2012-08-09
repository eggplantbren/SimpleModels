from pylab import *

x = linspace(-20., 20., 41)

# Noise-free data (i.e. model curve)
M = exp(-0.5*x**2) + 1./2*exp(-0.5*(x/2)**2) + exp(-0.5*(x - 2.7)**2)
M = M/M.sum()

# Noisy data
sig = 0.03
y = M + sig*randn(M.size)

plot(x, M, 'ko-', linewidth=2)
errorbar(x, y, yerr=sig*ones(y.size), fmt='bo')

ylim([-0.05*y.max(), 1.05*y.max()])
xlabel('Wavelength $\\lambda$', fontsize=14)
ylabel('Flux', fontsize=14)
show()

