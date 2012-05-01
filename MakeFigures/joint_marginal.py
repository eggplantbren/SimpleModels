from pylab import *
import copy

matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['legend.fontsize'] = 14
#matplotlib.rcParams['lines.linewidth'] = 2

xmin = -5.0
xmax =  5.0
ymin = -5.0
ymax =  5.0
n = 101

x = linspace(xmin, xmax, n)
y = linspace(ymin, ymax, n)
dy = y[1] - y[0]

[x, y] = meshgrid(x, y)
y = -y

prior = exp(-0.5*x[0,:]**2)
prior = prior/trapz(prior, x=x[0,:])
likelihood = exp(-0.5*(1.5 - x[0,:])**2)
posterior = prior*likelihood
posterior = posterior/trapz(posterior, x=x[0,:])

joint_prior = exp(-0.5*x**2)*exp(-0.5*(y-x)**2)
joint_prior = joint_prior/sum(joint_prior)

joint_posterior = copy.deepcopy(joint_prior)
which = nonzero(abs(y - 1.5) > 0.5*dy)[0]
joint_posterior[which] = 0.0
joint_posterior = joint_posterior/sum(joint_posterior)

figure(1, figsize=(10,10))
subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)

subplot(2,2,1)
plot(x[0,:], prior, 'r', label='Prior')
xlim([xmin, xmax])
ylim([0.0, 0.6])
xlabel('Parameters $\\theta$')
ylabel('Probability Density')
title('Prior (marginal view)')

subplot(2,2,2)
plot(x[0,:], posterior, 'k', label='Posterior')
plot(x[0,:], prior, 'r', label='Prior')
xlim([xmin, xmax])
ylim([0.0, 0.6])
legend(loc='upper left')
xlabel('Parameters $\\theta$')
ylabel('Probability Density')
title('Posterior (marginal view)')

subplot(2,2,3)
imshow(joint_prior, interpolation='nearest', extent=(xmin, xmax, ymin, ymax), aspect=1)
xlabel('Parameters $\\theta$')
ylabel('Data D')
title('Prior (joint view)')

subplot(2,2,4)
imshow(joint_posterior, interpolation='nearest', extent=(xmin, xmax, ymin, ymax), aspect=1)
xlabel('Parameters $\\theta$')
ylabel('Data D')
title('Posterior (joint view)')

savefig('joint_marginal.eps', bbox_inches='tight')

show()

