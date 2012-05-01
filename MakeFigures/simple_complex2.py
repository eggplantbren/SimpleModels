from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import fmin
import matplotlib
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['legend.fontsize'] = 14

def negative_entropy(params):
	global x, y_complex
	mu = params[0]
	lamb = params[1]
	nu = params[2]
	y_simple = (1.0 + lamb*(x - mu)**2/nu)**(-(nu + 1)/2.0)
	y_simple = y_simple/trapz(y_simple, x=x)
	return trapz(y_complex*log(y_complex/y_simple), x=x)

x = linspace(-5.0, 5.0, 301)
y_complex = exp(-abs(x/0.3)) + 0.3*exp(-0.5*((x-1.0)/0.5)**2)
y_complex = y_complex/trapz(y_complex, x=x)
params = array([0.0, 1.0, 5.0]) # Initial guess for t distribution parameters
			   # location, precision, degrees of freedom
params = fmin(negative_entropy, params)
mu = params[0]
lamb = params[1]
nu = params[2]
y_simple = (1.0 + lamb*(x - mu)**2/nu)**(-(nu + 1)/2.0)
y_simple = y_simple/trapz(y_simple, x=x)

plot(x, y_complex, label='Complex Reality')
plot(x, y_simple, 'r', label='Simple Model Fit')
xlabel('x')
ylabel('y')
legend(loc='upper left')
print(params)

savefig('simple_complex2.eps')

show()

