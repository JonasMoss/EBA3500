import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Make a random number generator
rng = np.random.default_rng(seed = 313)

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

## 1. Formulate a "pvals_left" function that calculates the p-value of the 
##    left-sided hypothesis test when sigma is known.

def pval(x, mu, sigma):
    """ Calculates the two-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return 1 - stats.halfnorm.cdf(np.abs(z))

def pval_left(x, mu, sigma):
    """ Calculates the left-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return 1 - stats.norm.cdf(z)

def pval_right(x, mu, sigma):
    """ Calculates the right-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return stats.norm.cdf(z)

pval_left([1.64], 0, 1)
pval_right([-1.64], 0, 1)

## 2. Do the six cases above using this p-value function too. (Make a guess
##    first!)

# Case 1: Same sigma, smaller mean.
n = 20
mu = 1
sigma = np.pi
n_reps = 10 ** 5
xx = rng.normal(0, sigma, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval_left,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()


## Case 3: Same mean, smaller sigma.
xx = rng.normal(1, 0.1, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval_left,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals >= 0.95)

## 3. Repeat exerise 1-2 for the right sided hypothesis test when sigma is known.
## Case 6: Large mean and a large sigma?
xx = rng.normal(2.5, np.pi ** 2, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval_right,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)
np.mean(pvals <= 0.01)

## Case 4: Same mean, bigger sigma.
xx = rng.normal(1, np.pi ** 2, (n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval_right,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)

## 4. Find another distribution to sample from and simulate the p-values as we
##    did in Case 1 - 6 (smaller and bigger standard deviation / smaller and bigger
##    mean). You don't need to be precise with the mean and sd (you can check 
##    them using functions in 'stats' or using simulation.) You should choose from
##    https://numpy.org/doc/1.16/reference/routines.random.html
##    (Hint: Find a distribution where you are able to calculate the mean and 
##    standard deviation, the formulas are available on wikipedia.) Laplace
##    is the easiest choice, but most of the distributions on that page will 
##    work. (Suggestion: Gamma, Weibull, Gumbel, log-normal.)

f_lnorm = lambda n: rng.lognormal(-2, 2, n) # Has "theoretical mean" equal to 1!

def f_lnorm(n):
    return rng.lognormal(-2, 2, n)

# But it has standard devation ~ 7.3

## Case 6: Large mean and a large sigma?
xx = f_lnorm((n_reps, n))

pvals = np.apply_along_axis(
    func1d = pval_right,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)
np.mean(pvals <= 0.01)

## Gumbel distribution

# Mean = 1, smaller variance

## The variance is less than 1 iff
## beta^2 < 6/pi^2.

beta = np.sqrt(0.2)

## Variance: 0.12158542037080532
mu = 1 - np.euler_gamma * beta
f_gumbel = lambda n: rng.gumbel(mu, beta, n)
x = f_gumbel(10 ** 6)

xx = f_gumbel((n_reps, n))
pvals = np.apply_along_axis(
    func1d = pval_right,
    axis = 1,
    arr = xx,
    mu = mu,
    sigma = sigma
)

sns.histplot(x = pvals, stat = "density")
plt.show()

np.mean(pvals <= 0.05)
np.mean(pvals <= 0.01)