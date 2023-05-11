### ============================================================================
### Are these numbers uniformly distributed?
### - Toy example, but take it seriously! 
### - An entrée to the introduction to p-values down the road.
### - Everyone misunderstands p-values, but you won't! ;-)
### ============================================================================

import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(seed = 313)

# Recall the uniform distribution:
x = rng.random(10 ** 5) # Or rng.uniform(0, 1, 100)
ax = sns.histplot(x = x, stat = "density")
ax.plot([0, 1], [1, 1], color = "black")
plt.show()

# Our toy question: If I generate n numbers, using numpy, can you check if 
# they're uniformly distributed? 
# Important: Suppose you have a good reason to believe x to be uniform!
# Before we begin, we'll have a look at the beta distribution, as it allows us
# to generate numbers that appear to be uniform.
# https://en.wikipedia.org/wiki/Beta_distribution
# This distribution lives on [0, 1] and takes two parameters.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html#numpy.random.Generator.beta

a = 0.5
b = 0.5
n = 10 ** 5
x = rng.beta(a, b, size = n) # the arguments are "reflective", in a sense
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(0, 1, 0.01)
ax.plot(xs, stats.beta(a, b).pdf(xs), color = "black")
plt.show()

# An example! I've used a numpy function and generated the following numbers.

x = np.array([5.70258616e-01, 1.31533851e-01, 7.15152445e-05, 1.52899760e-01,
       5.52929534e-01, 8.75248710e-01, 7.29185037e-01, 7.78659822e-01,
       9.60632819e-01, 6.61608144e-01, 6.59306121e-01, 4.85306505e-01,
       2.13916333e-05, 8.62834366e-01, 8.45059551e-01, 7.67764785e-03,
       6.12000371e-01, 4.15380394e-01, 9.50727491e-01, 4.48495141e-01,
       1.12312941e-01, 2.02838850e-03, 5.04186888e-01, 4.47375040e-01,
       3.20763388e-01, 9.18889642e-01, 9.26217971e-01, 9.45022807e-01,
       7.49472131e-02, 6.20486772e-01, 9.64122587e-01, 2.74248592e-01,
       6.92945084e-01, 9.10926599e-01, 2.37405564e-01, 5.07176445e-01,
       9.92052215e-01, 8.39082665e-02, 9.99131489e-01, 1.14400256e-01,
       1.95150958e-01, 8.98982929e-01, 7.91073000e-01, 9.32683299e-03,
       6.98481406e-01, 4.00702686e-01, 8.24043607e-01, 2.38324989e-01,
       1.64278558e-01, 5.57037069e-04, 4.32167708e-01, 2.43351328e-01,
       6.73839766e-03, 7.43803409e-01, 9.91462841e-01, 9.99786343e-01,
       3.00000957e-01, 3.28396752e-02, 8.05186886e-01, 6.87602404e-01,
       7.77879834e-01, 9.22076873e-01, 7.90439540e-01, 6.80337788e-01,
       7.49251014e-01, 8.40172810e-01, 8.15217327e-01, 6.94769055e-01,
       4.78705314e-01, 2.18637742e-01, 4.13961248e-01, 9.22767736e-01,
       9.21572409e-01, 4.03995188e-01, 3.43974446e-01, 2.74353761e-01,
       8.84677367e-01, 5.43038612e-01, 1.11842986e-01, 7.40130493e-01,
       3.00084282e-01, 9.66004675e-03, 7.97409085e-01, 9.97964861e-01,
       8.21165103e-01, 1.87903853e-01, 5.66298201e-04, 6.90456060e-01,
       2.30087756e-04, 3.95682990e-01, 8.43693640e-01, 7.76033497e-01,
       3.97624016e-01, 8.00115061e-01, 6.52866310e-01, 3.93230800e-01,
       4.87834036e-01, 7.61385466e-01, 4.65685489e-01, 9.90119067e-01])


# Are they uniform? It kinda looks like it.
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(0, 1, 0.01)
ax.plot(xs, stats.beta(1, 1).pdf(xs), color = "black")
ax.plot(xs, stats.beta(1, 3).pdf(xs), color = "blue")
plt.show()

# Important: Suppose you have a good reason to believe x to be uniform!
# For example, you may know me as a guy who's pretty fond of the uniform 
# distribution. (And quite fond of the beta(0.5, 0.5)!)

# Big problem: Every vector x has probability 0 under any continuous 
# distribution! Numerically, every vector x just has an incredibly small
# probability, no matter what the true generating distribution is.

# Idea: We know how to approximate the distribution of the mean, assuming the 
# numbers are uniformly distributed. Then we can check if observing a mean as
# large, or larger than, the mean we have observed, is probable or not.
# (We need this "or larger than" since observing a specific mean has probability
# 0 under the uniform distribution)

np.mean(x) # observed mean.

n_reps = 10 ** 5
n = 100
arr = rng.random((n_reps, n))
means = np.apply_along_axis(
    func1d = np.mean,
    axis = 1,
    arr = arr
)

sns.histplot(x = means, stat = "density")
plt.show()

# From this plot we see that the probability of the mean being greater than,
# say, 0.6, is small. Let's calculate how small it is.

np.mean(means >= 0.6) # How many observations are greater than 0.6?

# Can plot these probabilities for every x in the range of the data!
means_sorted = np.sort(means) # Returns a sorted copy x (in ascending order).
xs = np.arange(1, len(means) + 1) / (len(means) + 1)
plt.plot(means_sorted, 1 - xs)
plt.show()

# Let's try it on "x":
np.mean(x)
np.mean(means >= np.mean(x)) # 0.078

# But if beta(0.5, 0.5) is the true distribution, we wouldn't expect the means 
# to differ at all!

# On the other hand, the variance of beta(0.5, 0.5) appears to be larger, so
# let's try that one instead.

n_reps = 10 ** 5
n = 100
arr = rng.random((n_reps, n))
variances = np.apply_along_axis(
    func1d = np.var,
    axis = 1,
    arr = arr
)

np.var(x)
np.mean(variances) # 0.08
np.mean(variances >= np.var(x)) # 0.00281

# The probability of observering such a large variance, provided the true
# generator is uniform, is 0.0028. It's reasonable to think that
# x is not uniformly distributed.


# Task (i). Make a function test_rng. Its rng argument can be any random number
# generator, such as rng.standard_exponential used last time, but use
# rng.random to make it uniform!
def test_rng(x, func, rng, n_reps = 10 ** 5):
    """ Approximates the probability that func(y) >= func(x) when y is sampled 
    from rng. rng is the random number generator, e.g. the uniform distribution,
    and n_reps is the number of repetitions.
    """
    # FILL IN!
# Task (ii). Run test_rng on "x" using "median" and the functions we used 
# last time: sum(x ** 3), sum(exp(-x)), median(x) - mean(x), and 
# mean(abs(x - median(x))).
# Task (iii). Generate some data from the standard normal distribution and use
# test_rng to test if the data is probable under the normal distribution or not.
# Use the np.mean, np.var, and np.max as the function arguments.
# Task (iv). Suppose you knew that I like beta(9, 9) super-well, but never 
# generate data from beta(0.5, 0.5). How can you modify the variance approach
# above to work for data generated from beta(9, 9)? To solve this exercise you
# need to plot beta(9, 9)!