from pylab import *

figure(figsize=(8, 12))
seed(0)
x = linspace(-10., 10., 101)

M = exp(-0.5*(x/0.3)**2) + exp(-0.5*(x-1.)**2)
M = M/sum(M)
sig = 0.003*ones(M.shape)
y = M + sig*randn(M.size)

subplot(2,1,1)
plot(x, M, 'k.-', markersize=10)
xlabel('$x$', fontsize=24)
ylabel('Flux', fontsize=16)
plot([-10., 10.], [0., 0.], 'b')
ylim([-0.03, 0.13])
title('True Noise-Free Curve')

subplot(2,1,2)
errorbar(x, y, yerr=sig, fmt='ro', markersize=3)
xlabel('$x$', fontsize=24)
ylabel('Flux', fontsize=16)
plot([-10., 10.], [0., 0.], 'b')
ylim([-0.03, 0.13])
title('Noisy Data')

savefig('../emission_line.eps')
show()
