
from uniform import uniform
from exponential_distro import expo_distro
from normal_distro import normal_distro
from bernoulli_coin_flip import coin_flip
from discrete_uniform_dice_throw import dice_throw

from visualiser import hist_continiuous, bar_discrete, normal_with_pdf, expo_with_pdf, uniform_with_pdf, cdf_plot_norm, cdf_plot_expo, cdf_plot_uniform

from tests import normal_test, uniform_test, exponential_test



samples_uniform = uniform(5,10, 1_000_000)
hist_continiuous(samples_uniform, title = "Uniform(5,10)")
uniform_with_pdf(samples_uniform,a = 5,b = 10)
cdf_plot_uniform(samples_uniform, a=5, b = 10)


samples_expo = expo_distro(5,1_000_000)
hist_continiuous(samples_expo, title="Exponential (lambda = 5)")
expo_with_pdf(n_samples=samples_expo, lambda_parameter=5)
cdf_plot_expo(n_samples=samples_expo, lambda_parameter=5)


samples_normal = normal_distro(0,1, 1_000_000)
hist_continiuous(samples_normal, title= "Normal (mu = 0, sigma = 1)")
normal_with_pdf(samples_normal, mu = 0, sigma = 1)
cdf_plot_norm(samples_normal, mu=0, sigma = 1)


samples_coin = coin_flip(1_000_000)
bar_discrete(samples_coin, title = "Bernoulli coin flip")

samples_dice = dice_throw(1_000_000)
bar_discrete(samples_dice, title = "Discrete Uniform Dice")


u = uniform(5,10,1_000_000)
uniform_test(u, 5,10)

e = expo_distro(5,1_000_000)
exponential_test(e, 5)

n = normal_distro(0,1,1_000_000)
normal_test(n, 0,1)
