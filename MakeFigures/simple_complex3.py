from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import fmin
import matplotlib
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['legend.fontsize'] = 14

def negative_entropy(params):
	global x, y, z_complex
	mu_x = params[0]
	mu_y = params[1]
	sig = params[2]
	z_simple = exp(-0.5*((x - mu_x)**2 + (y - mu_y)**2)/sig**2)
	z_simple = z_simple/z_simple.sum()
	return sum(z_complex*log(z_complex/z_simple))

x = linspace(-4.0, 4.0, 101)
y = linspace(-4.0, 4.0, 101)
[x, y] = meshgrid(x, y)
y = -y

component1 = exp(-sqrt(x**2 + ((y+1)/0.5)**2))
component1 = component1/component1.sum()
component2 = exp(-0.5*((x - 1.0)**2 + (y - 0.5)**2))
component2 = component2/component2.sum()

z_complex = 0.5*component1 + 0.5*component2

params = array([0.0, 0.0, 1.0]) # Initial guess for gaussian parameters
			        # [mu_x, mu_2, sig]
params = fmin(negative_entropy, params)
mu_x = params[0]
mu_y = params[1]
sig = params[2]
z_simple = exp(-0.5*((x - mu_x)**2 + (y - mu_y)**2)/sig**2)
z_simple = z_simple/z_simple.sum()

imshow(z_complex, extent = [-4.0, 4.0, -4.0, 4.0])
contour(x, y, z_simple, 10, colors="white")
xlabel('x')
ylabel('y')

savefig('simple_complex3.eps')
show()


