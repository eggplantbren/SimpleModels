from numpy import *
from matplotlib.pyplot import *
import matplotlib
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['legend.fontsize'] = 12

x = linspace(-5.0, 5.0, 101)
L = exp(-0.5*x**2)
L_alternatives = [L**10, L**0.25, log(L+1.0), 1.0/(1.0 + exp(-L))]

subplot(2,1,1)
plot(x, L, linewidth=2)
for l in L_alternatives:
	plot(x, l/l.max(), '--')
ylabel('Likelihood')
xlim([-5.0, 5.0])
legend(('Formal Model', 'Alternatives'))

subplot(2,1,2)
p = [ones(x.shape)]
p[0] = p[0]/trapz(p[0], x=x)
limits = array([-5.0, 5.0])
mixture = p[0]
for i in xrange(0, 5):
	p_new = p[-1]
	which = nonzero(logical_or(x < limits[0], x > limits[1]))[0]
	p_new[which] = 0.0
	p_new = p_new/trapz(p_new, x=x)
	mixture = mixture + p_new
	p.append(p_new)
	limits = limits*0.5

mixture = mixture/trapz(mixture, x=x)
plot(x, mixture, 'k')


p = [ones(x.shape)]
p[0] = p[0]/trapz(p[0], x=x)
limits = array([-5.0, 5.0])
mixture = p[0]
for i in xrange(0, 20):
	p_new = p[-1]
	which = nonzero(logical_or(x < limits[0], x > limits[1]))[0]
	p_new[which] = 0.0
	p_new = p_new/trapz(p_new, x=x)
	mixture = mixture + p_new
	p.append(p_new)
	limits = limits*(10.0/11.0)

mixture = mixture/trapz(mixture, x=x)
plot(x, mixture, 'b')

xlabel('Parameters $\\theta$')
ylabel('Probability Density')
xlim([-5.0, 5.0])
savefig('nested.eps')
show()

