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

# We can n values from a normal distribution with standard deviation (sd) sigma
# mean mu. We can do this using "rng.normal(mu, sigma, n)"

mu = 1
sigma = 3
x = rng.normal(mu, sigma, 1)

# Let's plot this normal distribution
xs = np.linspace(mu - 2.5 * sigma, mu + 2.5 * sigma, 100)
plt.plot(xs, stats.norm.pdf(xs, mu, sigma), color = "black")
plt.vlines(x, ymin = 0, ymax = stats.norm.pdf(x, mu, sigma))
plt.show()

# Fundamental question: What can we say about the unknown mu from our known x?

# You must remember: mu is fixed and (usually) _unknown_ and x is random but 
# known.

## Normal confidence interval with known sigma.
# The classical alpha-level confidence interval for the mean is
# (*) [x_bar - z_alpha * sigma / sqrt(n), x_bar + z_alpha * sigma / sqrt(n)].
# Here n is the number of observations, x_bar is the empirical mean. Sigma is the
# KNOWN standard deviation, and z_alpha is the 1-alpha/2 quantile of the standard
# normal. (Recall, e.g., class notes 02.03: https://bit.ly/3qoytbH)

# An example of a 95% confidence interval:
n = 100
alpha = 0.05 # (0.95 = 1 - 0.05)
mu = 1 # this is "unknown" ;)
sigma = 3 # Known! Don't pretend you don't know.
x = rng.normal(mu, sigma, n)
x_bar = np.mean(x)
z_alpha = stats.norm.ppf(1 - alpha / 2) # ppf is the quantile function
# in scipy, this is called the percent point function; inverse of the cdf.
# this is apporximately 1.96 ~ 2.

plt.plot(xs, stats.norm.pdf(xs, 0, 1), color = "black")
plt.vlines([-z_alpha, z_alpha], ymin = 0, ymax = stats.norm.pdf(z_alpha, 0, 1))
plt.show()

# Using vectorization, we can calculate the confidence interval:
x_bar + np.array([-1, 1]) * z_alpha * sigma / np.sqrt(n)

# What is a 95% confidence interval?
# 1.) A confidence interval is a random variable that is a function of the 
# observed data (x in our case) and the known parameters (sigma in our case) only.
# 2.) The probability that the true parameter we care about (mu in our case) lies
# inside the confidence interval is equal to 95%, _no matter what the value of mu is_.

# Pre-data and post-data! The confidence interval is a pre-data construciton.
# So before you see my x, you know that your _confidence interval procedure_ will
# be so that the interval includes mu with probability 95%. But after you have 
# ovbserved an x, there is no probability. Why? x is observed and mu is observed.

# Now we'll simulate some intervals.

# We will start by making a function that calculates the intervals.
def ci(x, sigma = 1, alpha = 0.05):
    """ Calculate the two-sided confidence interval of size 1 - alpha for the
    mean in a a normal experiment when sigma is known."""
    n = len(x)
    x_bar = np.mean(x)
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    return(x_bar + np.array([-1, 1]) * z_alpha * sigma / np.sqrt(n))

# Now we want to simulate 1000s of CIs!
def simulator(mu, sigma, n, rng, n_reps = 10 ** 5):
    """ Simulate n_reps 95% confidence intervals when the data is normal with
    underlying mean mu, standard deviation sigma, and number of observations n.
    """
    x = rng.normal(mu, sigma, (n_reps, n))
    # The argument sigma is passed automatically to ci (func1d in general) using
    # the **kwargs construction. 
    # https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html
    return(np.apply_along_axis(func1d = ci, axis = 1, arr = x, sigma = sigma))

mu = 0
values = simulator(mu, sigma = 1, n = 100, rng = rng)

# We want to check if mu = 0 lies inside approximately 95% of these intervals!
# value[i, 0] <= mu <= value[i, 1].
values[:, 0] <= mu
mu <= values[:, 1]
True * True
True * False
False * False
np.mean((values[:, 0] <= mu) * (mu <= values[:, 1]))

def coverage(mu, sigma, n, rng, n_reps = 10 ** 5):
    """ Approximates the coverage of a 95% confidence interval for mu when sigma
    is known."""
    values = simulator(mu, sigma = sigma, n = n, rng = rng, n_reps = n_reps) 
    return(np.mean((values[:, 0] <= mu) * (mu <= values[:, 1])))

coverage(mu, 1, 10, rng) # Approximately 0.95 , mu = 0

# But remember, we want this approx 0.95 property to hold for every mu!
mus = np.linspace(-3, 3, 20)
coverages = np.array([coverage(mu, 1, 100, rng, 1000) for mu in mus])

# Plot this!
plt.plot(mus, coverages, color = "black")
axes = plt.gca()
axes.set_ylim([0, 1])
plt.hlines(0.95, xmin = -3, xmax = 3)
plt.show()

# Confidence intervals cannot be interpreted as anything easier than what I've
# just talked about: They are random intervals containing the true parameter mu
# with probability (say) 0.95, no matter what the true parameter is.
# On the exam: Don't give your intuition. 

# Hoekstra, R. et al (2014) list 6 common errors. Suppose you're given a confidence
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

### Task:
# 1.) What is the length of the confidence interval in (*)? (Length of [-3, 2] is 5.)
# 2.) Most confidence intervals, such as the t interval, does not have a fixed size.
#     make a fdunction that takes an array of CIs and returns the length of each CI.
# 3.) Explain why each point in the list of Hoekstra are errors. (Hint: There are
#     two kinds of mistakes in this list. First, they can talk about probabilities
#     when there is nothing random to talk about. Remember than mu is fixed. Second,
#     they think about the coverage (95% etc) of confidence intervals in terms of 
#     the observed intervals. Say if you have an observed interval  [-1, 1]. Then it isn't 
#     random -- it's [-1, 1]!).