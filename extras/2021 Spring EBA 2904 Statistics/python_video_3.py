### ============================================================================
### Histograms, densities, and the central limit theorem!
###  - Densities are a fundamental concept in statistics.
###    - Positive functions with area under the curve (integral) equal to 1.
###  - Simulating histograms helps us understand what densities are.
###  - We'll have a look at how to simulate normal data (and other data!)
###  - We demonstrate some cases of the central limit theorem:
###    (means of random variables are normally distributed)
###  - And make some exercises!
### ============================================================================

import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(seed = 313)

# Generate uniform random variables on [0, 1].
x = rng.random(10 ** 5) # Or rng.uniform(0, 1, 100)

# Make a histogram!
sns.histplot(x = x, stat = "density") # "density" makes the area equal to 1.
plt.show()

# The histogram is approximately constant, f(x) = 1, which is its density.
ax = sns.histplot(x = x, stat = "density")
ax.plot([0, 1], [1, 1], color = "black")
plt.show()

# The density is the shape of the historgram as n goes to infinity!

# What happens when n = 100?
x = rng.random(10 ** 2) # Or rng.uniform(0, 1, 100)
ax = sns.histplot(x = x, stat = "density")
ax.plot([0, 1], [1, 1], color = "black")
plt.show()

# Or when n = 40?
x = rng.random(40) 
ax = sns.histplot(x = x, stat = "density")
ax.plot([0, 1], [1, 1], color = "black")
plt.show()

# Normal distribution: https://en.wikipedia.org/wiki/Normal_distribution
x = rng.standard_normal(10 ** 5)

# for a list of distributions to generate from, see
# https://numpy.org/doc/stable/reference/random/generator.html

ax = sns.histplot(x = x, stat = "density")
xs = np.arange(-5, 5, 0.01)
ax.plot(xs, stats.norm.pdf(xs), color = "black")
plt.show()

# for a list of distributions to plot (and much more!), see
# https://docs.scipy.org/doc/scipy/reference/stats.html

# Exponential distribution: https://en.wikipedia.org/wiki/Exponential_distribution
x = rng.standard_exponential(10 ** 5) 
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(0, 10, 0.01)
ax.plot(xs, stats.expon.pdf(xs), color = "black")
plt.show()

# Discrete distributions are also possible.
# Binomal distribution: https://en.wikipedia.org/wiki/Binomial_distribution
x = rng.binomial(100, 0.3, 10 ** 5) 
uniques, counts = np.unique(x, return_counts = True)
xs = np.arange(1, 100, 1)
plt.bar(x = uniques, height = counts / 10 ** 5)
plt.plot(xs, stats.binom.pmf(xs, 100, 0.3), "ko")
plt.show()

### Let's simulate some means.

# Uniform variables on [0, 1]
n_reps = 10 ** 5
n = 1000
x = rng.random((n_reps, n))
means = np.apply_along_axis(
    func1d = np.mean,
    axis = 1,
    arr = x
)

sns.histplot(x = means, stat = "density")
plt.show()

# Exponential variables.
n_reps = 10 ** 5
n = 1000
x = rng.standard_exponential((n_reps, n))
means = np.apply_along_axis(
    func1d = np.mean,
    axis = 1,
    arr = x
)
sns.histplot(x = means, stat = "density")
plt.show()

#  Central limit theorem: "means" is approximately normally distributed!
# (It should be called "the central limit theorem", "det sentrale grenseteoremet".
# (the point is that the theorem is the most import, or central, limit theorem. 
# It's not about "central limits", whatever that means!)
# (It's "Der zentrale Grenzwertsatz" in german.)
# The normal distribution has two parameters, mean and standard deviation. 

ax = sns.histplot(x = means, stat = "density")
mean = np.mean(means)
# Var (X) = E(X^2) - E(X)^2
sd = np.sqrt(np.mean(means ** 2) - np.mean(means) ** 2)
xs = np.arange(mean - 3*sd, mean + 3*sd, 0.001)
ax.plot(xs, stats.norm.pdf(xs, mean, sd), color = "black")
plt.show()

# How about medians?
n_reps = 10 ** 5
n = 1000
x = rng.random((n_reps, n))
y = np.apply_along_axis(
    func1d = np.median,
    axis = 1,
    arr = x
)

ax = sns.histplot(x = y, stat = "density")
mean = np.mean(y)
# Var (X) = E(X^2) - E(X)^2
sd = np.sqrt(np.mean(y ** 2) - np.mean(y) ** 2)
xs = np.arange(mean - 3*sd, mean + 3*sd, 0.001)
ax.plot(xs, stats.norm.pdf(xs, mean, sd), color = "black")
plt.show()


# How about the variances?
n_reps = 10 ** 5
n = 1000
x = rng.random((n_reps, n))
y = np.apply_along_axis(
    func1d = np.var,
    axis = 1,
    arr = x
)
mean = np.mean(y)
sd = np.sqrt(np.mean(y ** 2) - np.mean(y) ** 2)
xs = np.arange(mean - 3*sd, mean + 3*sd, 0.001)
ax = sns.histplot(x = y, stat = "density")
ax.plot(xs, stats.norm.pdf(xs, mean, sd), color = "black")
plt.show()

### Tasks
# Task (i): Write down the body of the function that simulates and plots a 
# histogram and a normal density curve, just like we did above. (Generator can
# be e.g. rng.standard_exponential). Pass the "bins" to sns.histplot.
def clt(n, func, generator, n_reps, bins = None): # bins = None, bins = "auto"
    """ Simulates n values from generator n_reps times, applies func to the n
    values, then plots a histogram and normal density curve from the data."""
    y = generator((n_reps, n))
    ## FILL INN!
# Task (ii): Verify that the normal density curve approximates the histogram for
# the following functions: sum(x ** 3), sum(exp(-x)), median(x) - mean(x),
# mean(abs(x - median(x))). Do it for a couple of different generators chosen from 
# https://docs.scipy.org/doc/scipy/reference/stats.html, e.g. uniform, 
# standard exponential, and standard normal.
# Task (iii): Does the normal approximation work for the maximum or minimum? (np.max and np.min).
# Task (iv): Use the clt function with np.mean and the generator "standard_cauchy"
# and bins = 50. Why does this happen? 