## Simulating confidence intervals (ii)
## - In our last video we look at confidence intervals for the mean of 
##   normal variables.
## - But we assumed that the standard deviation was known. That's silly! In
##   practice we never known the sd.
## - The t interval doesn't assume a known sd though.
## - (i) We'll simulate data to check the coverage of the t interval and the normal
##   interval (using sample sd in place of the "known" sigma)!
## - (ii) Real data isn't perfectly normal. Does it matter for the validity of the 
##   confidence intervals? We'll simulate to find out.

import numpy as np
from scipy import stats

# Make a random number generator
rng = np.random.default_rng(seed = 313)

## Normal confidence interval with known sigma.
# The classical alpha-level confidence interval for the mean is
# (*) [x_bar - z_alpha * sigma / sqrt(n), x_bar + z_alpha * sigma / sqrt(n)].

## Normal confidence interval with unknown sigma: (t interval)
# (**) [x_bar - t_alpha * s / sqrt(n), x_bar + t_alpha * s / sqrt(n)]

# Two differences: s and sigma, t_alpha and z_alpha

# An example of a 95% confidence interval:
n = 20
alpha = 0.05
mu = 1
sigma = 3
x = rng.normal(mu, sigma, n)
x_bar = np.mean(x)
s = np.std(x, ddof = 1) # Must use "ddof = 1" to make std be based on the unbiased sample variance.
# sum((x - mean(x))^2) / len(x); sum((x - mean(x))^2) / (len(x) - 1)
z_alpha = stats.norm.ppf(1 - alpha / 2) # known sigma
t_alpha = stats.t.ppf(1 - alpha / 2, df = n - 1) # df : degrees of freedom.

x_bar + np.array([-1, 1]) * z_alpha * sigma / np.sqrt(n) # sigma known! impossible to use.
x_bar + np.array([-1, 1]) * z_alpha * s / np.sqrt(n) # "cheating interval"
x_bar + np.array([-1, 1]) * t_alpha * s / np.sqrt(n) # t-interval

## (i) Recall that the coverage of a confidence interval is the probability
##     that it contains the true parameter. We know from theory that the
##     coverage of the t interval is 95% (when alpha is chosen as above). The
##     coverage of the normal confidence interval should be smaller though. Here
##     we approximate the unknown sigma with s, the sample standard deviation.

def cis(x, alpha = 0.05):
    """Calculate the z and t intervals wth size 1 - alpha for the mean in a 
    normal experiment when sigma is unknown."""
    n = len(x)
    x_bar = np.mean(x)
    z_alpha = stats.norm.ppf(1 - alpha / 2) 
    t_alpha = stats.t.ppf(1 - alpha / 2, df = n - 1)
    s = np.std(x, ddof = 1)
    return(np.array([x_bar + np.array([-1, 1]) * z_alpha * s / np.sqrt(n) ,
    x_bar + np.array([-1, 1]) * t_alpha * s / np.sqrt(n)]))

cis(x)

def simulator(mu, sigma, n, rng, n_reps = 10 ** 5):
    """ Simulates n_reps 95% confidence intervals of the z-type and t-type with
    mean mu and standard deviation sigma, using n observations."""
    x = rng.normal(mu, sigma, (n_reps, n))
    return np.apply_along_axis(func1d = cis, axis = 1, arr = x)

simulator(0, 1, 20, rng, 100)

def coverage(mu, sigma, n, rng, n_reps = 10 ** 5):
    """ Approxmates the covarage of two 95% confidence inervals for mu whe 
    sigma is unknown."""
    values = simulator(mu, sigma, n, rng, n_reps)
    return {
        "z_interval" : np.mean((values[:, 0, 0] <= mu) * (mu <= values[:, 0, 1])),
        "t_interval" : np.mean((values[:, 1, 0] <= mu) * (mu <= values[:, 1, 1]))
    }

coverage(0, 1, 20, rng, 100)
# n_reps = 10 ** 5, n = 2, 5, 20, 100
rng = np.random.default_rng(seed = 313) # reproducibility!
coverage(0, 1, n = 2, rng = rng)
# 'z_interval': 0.70077, 't_interval': 0.95008}
coverage(0, 1, n = 5, rng = rng)
# {'z_interval': 0.87941, 't_interval': 0.95032}
coverage(0, 1, n = 20, rng = rng)
# {'z_interval': 0.93505, 't_interval': 0.94989}
coverage(0, 1, n = 100, rng = rng)
# {'z_interval': 0.94739, 't_interval': 0.95031}

# t_interval works well for all n, z_interval works well enough for large n, but
# performs poorly for small n.

## (ii) The t interval is often used for data that isn't normal. Is this fine
##     or not? We'll take a look at three different scenarios to investigate 
##     this.

# 1.) Exponential distribution
#     mean: 1/lambda [using lambda = 1]
#     https://en.wikipedia.org/wiki/Exponential_distribution

# 2.) Log-normal distributon
#     mean: exp(mu + sigma ^ 2 / 2) [using mu = -1 and sigma = sqrt(2)]
#     https://en.wikipedia.org/wiki/Log-normal_distribution

# 3.) t-distribution
#     mean: 0! (using df = 3)
#     https://en.wikipedia.org/wiki/Student%27s_t-distribution

# Use https://numpy.org/doc/1.16/reference/routines.random.html to simulate

f_exp = rng.standard_exponential # mean = 1
f_lnorm = lambda n: rng.lognormal(-1, np.sqrt(2), n) # mean = 1
f_t = lambda n: rng.standard_t(3, n) # using 3 because 2 is too small (mean = 0)

def simulator(n, f, n_reps = 10 ** 5):
    """ Simulate n_reps 95% confidence intervals when the data is distributed 
    according to f with number of observations n.
    """
    x = f((n_reps, n))
    return np.apply_along_axis(func1d = cis, axis = 1, arr = x)

simulator(10, f_t, 100)
simulator(10, f_exp, 100)
simulator(10, f_lnorm, 100)

def coverage(n, f, mu, n_reps = 10 ** 5):
    """ Approximates the coverage of the two 95% confidence interval for mu when
        sigma isn't known, the true data generating mechanism is f, and the true
        mean is mu. """
    values = simulator(n, f, n_reps)
    return {
        "z_interval" : np.mean((values[:, 0, 0] <= mu) * (mu <= values[:, 0, 1])),
        "t_interval" : np.mean((values[:, 1, 0] <= mu) * (mu <= values[:, 1, 1]))
    }

coverage(10, f_t, 0, n_reps = 100)
coverage(10, f_exp, 1, n_reps = 100)
coverage(10, f_lnorm, 1, n_reps = 100)

# n = 5, 10, 100. n_reps = 10 ** 5

coverage(5, f_t, 0) # {'z_interval': 0.93174, 't_interval': 0.98131}
coverage(10, f_t, 0) # {'z_interval': 0.95915, 't_interval': 0.98094}
coverage(100, f_t, 0) # {'z_interval': 0.97735, 't_interval': 0.97936}

coverage(5, f_exp, 1) # {'z_interval': 0.80953, 't_interval': 0.88297}
coverage(10, f_exp, 1) # {'z_interval': 0.87244, 't_interval': 0.90195}
coverage(100, f_exp, 1) # {'z_interval': 0.9386, 't_interval': 0.94146}

coverage(5, f_lnorm, 1) # {'z_interval': 0.63744, 't_interval': 0.71256}
coverage(10, f_lnorm, 1) # {'z_interval': 0.70687, 't_interval': 0.74013}
coverage(100, f_lnorm, 1) # {'z_interval': 0.86169, 't_interval': 0.86448}

# Tentative conclusion: t-interval works better than the z-interval. Both 
# intervals are reasonable when n is large enough (except for lognormal.) 
# But neither are perfect for _skewed_ distributions.

# (i) Find the formula for the mean and variance of a log-normal at the 
#     wikipedia page https://en.wikipedia.org/wiki/Log-normal_distribution. 
#     Do the coverage simulation for a choice of parameters mu, sigma where
#     the variance is large. (Find the mean too!)
# (i*) Run the coverage simulation for n = 1000 too!
# (ii) Do the coverage experiment for the Gumbel distribution. That involves:
#      finding the mean of the Gumbel and how to simulate from it. 
# (iii) Make a plot of the coverage for the t-interval versus n for n = [5, 10,
#      20, 50, 100, 200, 1000] for the exponential case.
