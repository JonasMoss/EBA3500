## Simulating hypothesis tests and p-values (i)
## 
## - Recall the definition of an observed p-values: 
##       "The probability of observing something at least as extreme as what we
##        have observed, given that the null-hypothesis is true."
## - Often the null-hypothesis is just a single probability measure, or model,
##   which makes it easy to simulate the behavior of p-valuess under the
##   null-hypothesis.
## - In this video we will simulate p-values. We will focus on one particular
##   feature of p-values when the null-hypothesis is true, namely that they
##   are uniform. See the attached pdf for details.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Make a random number generator
rng = np.random.default_rng(seed = 313)

## Verify the Z-test (that is normally distributed)
n = 20
mu = 1
sigma = np.pi # 3.14....
x = rng.normal(mu, sigma, n)
x_bar = np.mean(x)
z = np.sqrt(n) * (x_bar - mu)/sigma

## Many iterations; verify normality.
n_reps = 10 ** 5
xx = rng.normal(mu, sigma, (n_reps, n))
zz = np.apply_along_axis(
    func1d = lambda x: np.sqrt(n) * (np.mean(x) - mu)/sigma,
    axis = 1,
    arr = xx
)

ax = sns.histplot(x = zz, stat = "density")
ax.plot(sorted(zz), stats.norm(0, 1).pdf(sorted(zz)), color = "black")
plt.show()

plt.plot(sorted(zz), stats.halfnorm.pdf(sorted(zz)), color = "black")
plt.show()


## Verify the Z-test (that is normally distributed)
n = 20
mu = 1
sigma = np.pi # 3.14....
x = rng.normal(mu, sigma, n)
x_bar = np.mean(x)
z = np.sqrt(n) * (x_bar - mu)/sigma
p = 1 - stats.halfnorm.cdf(np.abs(z)) # halfnorm is the halfnormal distribution.

def pval(x, mu, sigma):
    """ Calculates the two-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return 1 - stats.halfnorm.cdf(np.abs(z))

# And simulate a lot of p-values.
n = 20
n_reps = 10 ** 5
mu = 1
sigma = np.pi
xx = rng.normal(mu, sigma, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show()

## How about the probability of observing a p-value less than 0.27?
np.mean(pvals <= 0.27)

## What happens when the null hypothesis is false?

# Case 1: Same sigma, smaller mean.
n = 20
mu = 1
sigma = np.pi
n_reps = 10 ** 5
xx = rng.normal(0, sigma, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

# Case 2: Same sigma, bigger mean.
n = 20
mu = 1
sigma = np.pi
n_reps = 10 ** 5
xx = rng.normal(2.5, sigma, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)

## Case 3: Same mean, smaller sigma.
xx = rng.normal(1, 0.1, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals >= 0.95)

## Case 4: Same mean, bigger sigma.
xx = rng.normal(1, np.pi ** 2, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)

## Case 5: Large mean and a small sigma?
xx = rng.normal(2.5, 0.1, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)

## Case 6: Large mean and a large sigma?
xx = rng.normal(2.5, np.pi ** 2, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)
np.mean(pvals <= 0.01)

## Tasks
## 1. Formulate a "pvals_left" function that calculates the p-value of the 
##    left-sided hypothesis test when sigma is known.
## 2. Do the six cases above using this p-value function too. (Make a guess
##    first!)
## 3. Repeat exerise 1-2 for the right sided hypothesis test when sigma is known.
## 4. Find another distribution to sample from and simulate the p-values as we
##    did in Case 1 - 6 (smaller and bigger standard deviation / smaller and bigger
##    mean). You don't need to be precise with the mean and sd (you can check 
##    them using functions in 'stats' or using simulation.) You should choose from
##    https://numpy.org/doc/1.16/reference/routines.random.html
##    (Hint: Find a distribution where you are able to calculate the mean and 
##    standard deviation, the formulas are available on wikipedia.) Laplace
##    is the easiest choice, but most of the distributions on that page will 
##    work. (Suggestion: Gamma, Weibull, Gumbel, log-normal.)

