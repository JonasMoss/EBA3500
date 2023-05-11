### ============================================================================
### Random walks! ("Virrevandring")
###  - Random walks are helpful in understanding probability and simulation.
###  - Conceptual foundation of mathematical finance.
###  - "A Random Walk Down Wall Street" (Malkiel) - 1.5 million copies sold
###  - Used to think about the movement of e.g. stock prices.
### ============================================================================

import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)

n = 100
# Simulate integers -1, 0, 1 with equal probability (1/3).
z = rng.integers(low = -1, high = 2, size = n)
sns.scatterplot(x = range(1, n + 1), y = z)
plt.show()

# A random walk is defined like this:
# b_0 = z_0
# b_i = b_(i - 1) + z_i = z_1 + z_2 + ... + z_i

# np.cumsum(z) "cumulative sum" makes an array where the ith element is the sum
# of the i first elements of z:
b = np.cumsum(z) 

# A _much_ faster way of doing:
b_ = [sum(z[0:i]) for i in range(1, n + 1)]

# The speed difference matters in simulation studies!

# b is a "realized random walk".
# Let's plot it.
sns.scatterplot(x = range(1, n + 1), y = b)
plt.show()

# For each i, the theoretical mean (expected value) of z_i is 0.  To see why,
# the expected value equals 1/3*-1 + 1/3*0 + 1/3*1 = 0. Let's calculate the 
# rolling means of z: m[i] = mean(z[0:(i + 1)])

n = 5000 # More fun with larger n!
b = np.cumsum(rng.integers(low = -1, high = 2, size = n))
graph = sns.scatterplot(
    x = range(1, n + 1), 
    y = b / np.arange(1, n + 1)) # We're calculating the rolling means here.
graph.axhline(0)
plt.show()

# Such a random walk is always between -n and n. Moreover, each realized random
# walk has a maximum. 
np.max(b)

# Let's add it to the plot too. 
graph = sns.scatterplot(x = range(1, n + 1), y = b)
graph.axhline(np.max(b))
plt.show()

# Use np.argwhere to find the indices of the maxima.
np.argwhere(b == np.max(b))

# But what is the distribution of the maximas after n steps, i.e, the 
# probability that max(b) = i for every -n <= i <= n? Let's see.


def walk_max(n, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "result" is the maximum value of a random 
    walk and "probability" is the probability of achieving that result.

    Warning! Don't use too large n or n_reps; you'll run out of memory. Memory
    usage is 8 * n * n_reps bytes.

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """

    bs = np.apply_along_axis(
        func1d = np.cumsum, 
        axis = 1, 
        arr = rng.integers(low = -1, high = 2, size = (n_reps, n)))

    # NB: This one is approximately 800 mb big! (n_reps = 10 ** 5, n = 1000)
    # Due to the way numpy works, memory issues are unavoidable when 
    # simulating a lot of data. It's possible to do the simulations without 
    # using an iota of memory, but the we'd have to sacrifice speed big time! 
    # (Or do it in C++ / C / some low-level language.)  

    results = np.apply_along_axis(
        func1d = np.max, 
        axis = 1, 
        arr = bs)     

    # ... but this one is only 800 kb. =)

    uniques, counts = np.unique(results, return_counts = True)
    return {"result" : uniques, "probability" : counts / n_reps}

simulated_maxima = walk_max(1000, rng = rng)
sns.barplot(
    x = "result", 
    y = "probability", 
    data = simulated_maxima)
plt.show()

result = simulated_maxima["result"]
probabilities = simulated_maxima["probability"]

e_z = np.sum(result * probabilities)
# var(z) = E(z^2) - E(z)^2
sd_z = np.sqrt(np.sum(result ** 2 * probabilities) - e_z ** 2)


# Tasks: 
# (1) Modify walk_max to approximate the distribution of the maximal sum of
#     three ajacent values of the random walk.
# Hint: To calculate the sum of all k adjacent values in a 1-dimensional array x
#       use np.convolve(x, np.repeat(1, k), mode = 'valid'). For instance

x = np.arange(1, 10)
y = np.convolve(x, np.repeat(1, 3), mode = 'valid')

# (2) Calculate the vector with values x[0] = b[0], x[i + 1] = b[i + 1] - b[i]
#     directly. Is there a better way to calculate this vector? (Both by
#     standard Python and by numpy!)
# (3) Calculate the expectation and variance of the maximal sum of three 
#     adjacent values you found in task (i). Remember to use a small n.
# (4) (Harder!) Make a function that approximates the distribution of the 
#     following random variable. Some random walks with n > 10 steps will 
#     cross the number 10 (that is b > 10) at some point, some won't. Now consider only the 
#     random walks that crosses 10 at some point and approximate the probability 
#     that they cross 10 again. Remember the docstring and make it so that both
#     m = 10 and n are arguments to the function. Use small ns to make the
#     simulation run in a reasonable amount of time. (And memory!)


# Explaing 4:
n = 500
b = np.cumsum(rng.integers(low = -1, high = 2, size = n))
graph = sns.scatterplot(x = range(1, n + 1), y = b)
graph.axhline(10)
plt.show()