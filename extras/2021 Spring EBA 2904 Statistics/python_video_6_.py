## Simulating confidence intervals (i)
## - Will simulate one of the confidence intervals you've been exposed to.
## - Provide some intuition about what happens!
## - NB! If you Google confidence intervals, plenty of explanations will be 
##   wrong, maybe even most. I think 70% of psychology textbooks give a wrong
##   definition.

import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

# Make a random number generator
rng = np.random.default_rng(seed = 313)

# We can simulate n values from a normal distribution with variance sigma and 
# mean mu using "rng.normal(mu, sigma, n)"
mu = 1 
sigma = 3
x = np.random.default_rng().normal(mu, sigma, 1)

# Moreover, we can plot a normal desnity with these parameters:
xs = np.arange(mu - 2.5 * sigma, mu + 2.5 * sigma, 0.01)
plt.plot(xs, stats.norm.pdf(xs, mu, sigma), color = "black")
plt.show()

# ... and add our observation x to this plot:
plt.plot(xs, stats.norm.pdf(xs, mu, sigma), color = "black")
plt.vlines(x, ymin = 0, ymax = stats.norm.pdf(x, mu, sigma))
plt.show()

## Fundamental question: What can we say about mu from one or more observations
## of x?

## Remember: mu is fixed (and usually unknown), x is random and known!

## Normal confidence intervals with known sigma
# The classical alpha-level confidence interval for the mean is
# (*) [x_bar - z_alpha * sigma / sqrt(n), x_bar - z_alpha * sigma / sqrt(n)],
# where n is the number of observations, x_bar the empirical mean, sigma the
# KNOWN standard deviation, and z_alpha is the 1 - alpha/2 quantile of the
# standard normal. (Recall, e.g., class notes 02.03: https://bit.ly/3qoytbH

# An example 95% confidence interval:
n = 100
alpha = 0.05
mu = 1 # "Unknown" :-)
sigma = 3 # Known!
x = np.random.default_rng().normal(mu, sigma, n) 
x_bar = np.mean(x)
z_alpha = stats.norm.ppf(1 - alpha / 2) # approximately 1.96, approximatel 2!
# The method "ppf" is the quantile function, called percent point function in
# scipy.

plt.plot(xs, stats.norm.pdf(xs, 0, 1), color = "black")
plt.vlines(z_alpha, ymin = 0, ymax = stats.norm.pdf(z_alpha , 0, 1))
plt.vlines(-z_alpha, ymin = 0, ymax = stats.norm.pdf(z_alpha , 0, 1))
plt.show()

# Using vectorization, the confidence interval becomes:
x_bar + np.array([-1, 1]) * z_alpha * sigma / np.sqrt(n)

# What is a 95% confidence interval?
# 1.) A confidence interval is a random interval that is a function of the
# observed data (x in our case) and _known_ parameters (sigma in our case) only.
# 2.) The probability that the true parameter we care about (mu = 1) lies inside 
# the confidence interval is equal to 95%, _no matter what the true parameter is_.

# Now we'll simulate a bit to make the second point clearer.

# First we need a function to calculate a confidence interval (CI).
def ci(x, sigma = 1, alpha = 0.05):
    """Calculate the two-sided confidence interval of size 1 - alpha for the 
    mean in a normal experiment where sigma is known. """
    x_bar = np.mean(x)
    z_alpha = stats.norm.ppf(1 - alpha / 2) 
    return(x_bar + np.array([-1, 1]) * z_alpha * sigma / np.sqrt(n))

# Then we need to simulate thousands of them.
def simulator(mu, sigma, n, rng, n_reps = 10 ** 5):
    """Simulates n_reps 95% confidence intervals when the data is normal with 
    underlying mean mu, standard deviation sigma and number of observations
    n."""

    x = np.random.default_rng().normal(mu, sigma, (n_reps, n)) 
    # The argument sigma is passed to ci automatically. See *kwargs
    # https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html
    return(np.apply_along_axis(func1d = ci, axis = 1, arr = x, sigma = sigma))

mu = 0
values = simulator(mu, 1, 100, rng)

# We want to to check if mu = 0 lies inside each of these intervals!

values[:, 0] <= mu) 
np.mean(values[:, 0] <= mu))
mu <= values[:, 1])
np.mean(mu <= values[:, 1]))
True * True
True * False
False * False
# a <= x <= b is (a <= x) * (x <= b)!
np.mean((values[:, 0] <= mu) * (mu <= values[:, 1])) # Is mu inside values?

def coverage(mu, sigma, n, rng, n_reps = 10 ** 5):
    """ Approximates the coverage of a 95% confidence interval for mu when sigma
    is known.""" 
    x = np.random.default_rng().normal(mu, sigma, (n_reps, n)) 
    values = np.apply_along_axis(func1d = ci, axis = 1, arr = x, sigma = sigma)
    return(np.mean((values[:, 0] <= mu) * (mu <= values[:, 1])))

mus = np.linspace(-3, 3, 20)
coverages = np.array([coverage(mu, 1, 100, rng, 1000) for mu in mus])
plt.plot(mus, coverages, color = "black")
axes = plt.gca()
axes.set_ylim([0, 1])
plt.hlines(0.95, xmin = -3, xmax = 3)
plt.show()

### Why does this happen?
# 1.) If X is normal with mean 0 and sd 1, aX + b is normal with sd a and mean
#     b.
# 2.) Moreover, the sum of iid normals with the same mean (b) and sd (a) is 
#     normal with mean b and sd a * sqrt(n). 
# 3.) In addition, the mean of such iid normals have mean b and sd a / sqrt(n).
# 4.) Combined, this tells us that sqrt(n) * (x_bar - mu) / sigma is standard
#     normal, no matter what the true mu is! This is called a statistical pivot. 
# 5.) This exact phenomenon extremely uncommon, but quite common to hold 
#     approximately, in large samples.

# Confidence intervals can't really be interpreted as anything else than
# a random interval that contains the true parameter with probabilitity 1 - alpha.
# If you're asked about explaining CIs at the exam, for instance, just give the
# mathematical definition, as your interpretation is likely to be wrong.

# Hoekstra, R. et al list 6 common errors. Suppose you're given a confidence
# interval for the mean equal to [0.4, 0.6]. Which of the following is true?
# 1. The probability that the true mean is greater than 0 is at least 95 %.
# 2. The probability that the true mean equals 0 is smaller than 5 %.
# 3. The “null hypothesis” that the true mean equals 0 is likely to be incorrect.
# 4. There is a 95 % probability that the true mean lies between 0.1 and 0.4.
# 5. We can be 95 % confident that the true mean lies between 0.1 and 0.4.
# 6. If we were to repeat the experiment over and over, then 95 % of the time the 
#    true mean falls between 0.1 and 0.4.
# Interested readers can have a look at (this is not on the curriculum.)
# Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). 
# Robust misinterpretation of confidence intervals. 
# Psychonomic Bulletin & Review, 21(5), 1157–1164. 
# https://doi.org/10.3758/s13423-013-0572-3


### Tasks.
# 1.) What is the length of the confidence interval in (*)?
# 2.) When sigma = 1, what is the number of observations needed to make the
#     length of the interval equal to 0.5? (95% confidence interval)
# 3.) Most confidence intervals, such as the t interval, does not have a 
#     fixed size. Make a function that takes an array of CIs (such as values
#     above) and returns the leNngth of each interval in the array.
# 4.) (Hard?) Explain why all the interpretations of confidence intervals above
#     are wrong. (Hint: There are two kinds of errors involved. Either the 
#     statements assign probabilities to non-random quantities (such as the
#     true mean), or they handle the _random_ confidence interval as a fixed
#     quantitiy.)
