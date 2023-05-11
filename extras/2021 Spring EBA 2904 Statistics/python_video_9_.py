## Simulating hypothesis tests and p-values (ii)
## 
## - Recall the definition of an observed p-values: 
##       "The probability of observing something at least as extreme as what we
##        have observed, given that the null-hypothesis is true."
## - Last time we had a look at the distribution of p-values when the 
##       nullhypothesis is simple. In in that case it was possible to simulate
##       from the unique null hypothesis.
## - However, the null-hypohthesis is often not unique!

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Make a random number generator
rng = np.random.default_rng(seed = 313)

# Recall the one-sample t test. Assuming X_1, X_2, ..., X_n are normal with mean
# mu_0 and an unknown standard deviation sigma, the t-test has hypotheses
# 
#   H_0: the true mean mu_0 equals 0,
#   H_a: the true mean mu_0 is something else than 0.
#
# But H_0 contains many distribution, for instance rng.normal(0, 1) and
# rng.normal(0, 2). If sigma > 0, then rng.normal(0, sigma) is in H_0. This
# makes it impossible to simulate from the whole of H_0, as it's infinitely large.

def pval(x):
    """ Calculates the two-sided p-value for H_0: mu = 0 based on the t-test."""
    x_bar = np.mean(x)
    n = len(x)
    s = np.std(x, ddof = 1)
    t = np.sqrt(n) * x_bar/s
    return 2 * stats.t.cdf(-np.abs(t), n - 1)

pval(rng.normal(0, 1, 100))

# This is a p-value for any standard deviation (sd), we know this due to math.
# It's impossible to verify for every sd, but we can check it for some, e.g.
# 0.5, 1, and 13.37

def sim_pvals(n, sigma, n_reps = 10 ** 5):
    """ Generate n observations from a normal with standard deviation sigma and
    mean 0, then calculate the two-sided p-value bases on the the t_test. Do
    this n_reps time. 
    
    The null-hypothesis is that mu = 0; but this is not unique, as sigma 
    can vary. """
    return np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = rng.normal(0, sigma, (n_reps, n)))

# Try this with sigma = 0.5, 1, and 13.37
pvals = sim_pvals(10, 0.5)
ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show()

# It's appears to be true for these sigma, but could be false for other sigma,
# such as sigma = pi ** pi ** pi ** pi.

# NB: The p-value won't hold for distributions other than the normal! 

# Recall the log-normal distribution: 
f_lnorm = lambda n: rng.lognormal(-1, np.sqrt(2), n) # has mean 1!

# This density has sd ~ 2.5.

n_reps = 10 ** 5
n = 100

pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_lnorm((n_reps, n)) - 1)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

# Too big chance to reject!

# The mean of the lognormal is exp(mu + sigma ** 2 / 2),
# where mu and sigma are the "log"-parameters plugged into
# rng.lognormal (i.e, rng.lognormal(mu, sigma, n))
# Thus, rng.lognormal(-2, 2, n) has mean exp(-2 + 2 ** 2 / 2) = 1,
# too, but has a different standard deviation. (See wikipedia.)
# (sd ~ 7.3)

f_lnorm = lambda n: rng.lognormal(-2, 2, n) # has mean np.exp(3)!
n_reps = 10 ** 5
n = 100
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_lnorm((n_reps, n)) - 1)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

# Tasks:
# (i) Simulate p-values using a log-normal with standard deviation 100. Remember
#     to subtract the mean! 
# (ii) Simulate p-values from a Laplace distribution with mean 0 (see the docs at
#     https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html)
#     with scale parameter 0.1, 1, and 13.37. How does the t-test perform? Does
#     it care about the standard deviation?
# (iii) Simulate p-values from a uniform distribution (subtract 1/2 from the variates
#     to make the mean equal to 0). How well does it work? 
# (iv) Find the expression for the standard deviation of the uniform distribution.
#     Sample random variables from the uniform distributio on [-1, 1], [-30, 30],
#     and [-1000, 1000]. How well does the t-test work? Is it affected by the
#     standard deviation? (Hint: To generate variates
#     from these distributions, first generate the values "sims", then subtract -1/2,
#     then multiply by 2 * a, where a is the desired number. For instance to simulate
#     from [-30, 30], you would use 60 * (sims - 1/2)). 