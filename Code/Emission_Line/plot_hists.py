from pylab import *

flux1 = loadtxt('flux1.txt')
flux2 = loadtxt('flux2.txt')

hist(flux1, 20, normed=True, histtype='step', label='$\\sigma$-boost included', linewidth=2)
hist(flux2, 20, normed=True, histtype='step', label='$\\sigma$-boost not included', color='r', linewidth=2)
xlim([0.9, 1.1])
ylim([0, 120])
plot([1, 1], [0, 120], 'k--', linewidth=2, label='True Value')
legend()
xlabel('Total Flux', fontsize=14)
ylabel('Posterior Probability', fontsize=14)
show()

savefig('../failure.eps')

