## Simulating confidence intervals (ii)

# (i) Find the formula for the mean and variance of a log-normal at the 
#     wikipedia page https://en.wikipedia.org/wiki/Log-normal_distribution. 
#     Do the coverage simulation for a choice of parameters mu, sigma where
#     the variance is large. 

mu = 0
sigma = 3
mean_lnorm = np.exp(mu + sigma ** 2 / 2) # mean
(np.exp(sigma ** 2) - 1) * np.exp(2 * mu + sigma ** 2) # variance
f_lnorm = lambda n: rng.lognormal(mu, sigma, n)

np.mean(f_lnorm(10 ** 6))

coverage(100, f_lnorm, mean_lnorm) # {'z_interval': 0.44996, 't_interval': 0.4525}

# (ii) Do the coverage experiment for the Gumbel distribution. Look up the 
#     Gumbel distribution at wikipedia to find the formula for the true mean.
#     https://numpy.org/doc/1.16/reference/generated/numpy.random.gumbel.html#numpy.random.gumbel
#     https://en.wikipedia.org/wiki/Gumbel_distribution

mu = 3
beta = 4
mean_gumbel = mu + beta * np.euler_gamma
f_gumbel = lambda n: rng.gumbel(mu, beta, n)

coverage(100, f_gumbel, mean_gumbel) {'z_interval': 0.94457, 't_interval': 0.94725}

# (iii) Make a plot of the coverage of the t-interval versus n for 
#     n = [5, 10, 20, 50, 100, 200, 1000] for the exponential case.

ns = np.array([5, 10, 20, 50, 100, 200, 1000])
f_exp = rng.standard_exponential
ys = np.array([coverage(n, f_exp, 1, n_reps = 1000)["t_interval"] for n in ns])

plt.plot(ns, ys)
plt.show()



