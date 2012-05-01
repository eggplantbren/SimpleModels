from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import fmin
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['legend.fontsize'] = 14

def chisq(params):
	global x, y_complex
	m = params[0]
	b = params[1]
	y_simple = m*x + b
	return trapz((y_simple - y_complex)**2, x=x)

x = linspace(-5.0, 5.0, 301)
y_complex = x + sin(2*pi*x/4.0) - 0.15*x**2
params = array([0.0, 0.0]) # Initial guess for straight line
params = fmin(chisq, params)
m = params[0]
b = params[1]
y_simple = m*x + b

plot(x, y_complex, label='Complex Reality')
plot(x, y_simple, 'r', label='Simple Model Fit')
xlabel('x')
ylabel('y')
legend(loc='upper left')

savefig('simple_complex1.eps')

show()

