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

# Recall the one-sample t test. Assuming X_1, X_2, ..., X_n are normal with
# mean mu_0  and unknown standard deviation sigma, the t-test has the hypotheses
#       H_0: the true mean equals 0 (mu_0 = 0),
#       H_a: the true mean is unequal to 0.
#
# There are many distributions in H_0: E.g., rng.normal(0, 1, n), rng.normal(0, pi, n),
# rng.normal(0, 2, n). ANY rng.normal(0, x, n) is in H_0 if x > 0. It is impossible
# from all the distributions in H_0, as it is infiniely large!

def pval(x):
    """ Calculate the two-sided p-value for h_0: mu = 0, based on the t-est."""
    x_bar = np.mean(x)
    n = len(x)
    s = np.std(x, ddof = 1)
    t = np.sqrt(n) * x_bar / s
    return 2 * stats.t.cdf(-np.abs(t), n - 1)

pval(rng.normal(0, 1, 100))

# This is a p-value for any standard deviation (sd), we know this due to math.
# It's impossible to verify by simulation that this is a p-value for every choice
# of sd. But we can try it out for some values, such as 0.5, 1, 13.37.

def sim_pvals(n, sigma, n_reps = 10 ** 5):
    """ Generates n observations from a normal with standard deviation sigma and 
    mean 0, then calculates a two-sided (t-test) p-value for these observations.
    We repeat this n_reps times."""

    return np.apply_along_axis(
            func1d = pval,
            axis = 1,
            arr = rng.normal(0, sigma, (n_reps, n))
    )

# Let's try it out fro sigma = 0.5, 1, and 13.37
pvals = sim_pvals(10, 0.5)
ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(pvals), color = "black")
plt.show()

pvals = sim_pvals(10, 13.37)
ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(pvals), color = "black")
plt.show()

# BUT if we didn't know theory, it could have been that our proposed p-value wasn't
# actually a p-value for for instance say, pi ** pi ** pi ** pi.

# Recall that the p-value is guaranteed to hold only for normally distributed variables!

# Recall the log-normal distributions:
f_lnorm = lambda n: rng.lognormal(-1, np.sqrt(2), n) # Has "theoretical mean" equal to 1!

# (We can verify that the standard deviation is approximately 2.5)

n = 10
n_reps = 10 ** 5
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_lnorm((n_reps, n)) - 1
)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(pvals), color = "black")
plt.show()

# We know that the mean of the lognormal is equal to exp(mu_ + sigma_ ** 2 / 2)
# where mu_ and sigma_ are the "log"-parameters of a lognormal, i.e. 
# rng.lognormal(mu_, sigma_, n).
# For istance, rng.lognormal(-2,2,n) has mean exp(-2 + 2 ** 2 / 2) = 1.
# But it has standard devation ~ 7.3

f_lnorm = lambda n: rng.lognormal(-2, 2, n) # Has "theoretical mean" equal to 1!

n = 10
n_reps = 10 ** 5
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_lnorm((n_reps, n)) - 1
)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(pvals), color = "black")
plt.show()

## Task:
## (i) Simulate p-values from a log-normal with sd = 100! (Remember to subtract
##     the mean.) (Find the expression for the standard deviaiton on wikipedia.)
## (ii) Simulate p-values from the Laplace distribution. (see the docs at
##     https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html)
##     Use scale parameter = 0.1, 1, 13.37. (Use location = 0, this is the mean.
##     How well does the t-test work? Does it work differently for different scales?
## (iii) Simulate p-values from a uniform distribution. (Here you have to subtract 1/2 in order
##     to make the mean equal to 0.)
## (iv) Find the expression for the standard deviation of the uniform distribution. (On [0, 1]).
##     Sample random variables from the uniform distributio on [-1, 1], [-30, 30],
##     and [-1000, 1000]. How well does the t-test work? Is it affected by the
##     standard deviation? (Hint: To generate variates
##     from these distributions, first generate the values "sims", then subtract -1/2,
##     then multiply by 2 * a, where a is the desired number. For instance to simulate
##     from [-30, 30], you would use 60 * (sims - 1/2)). 
