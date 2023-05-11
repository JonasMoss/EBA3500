# In this tutorial we'll take a look at how to simulate dice throws in Python!
# Two things to keep in mind:
#   i)  Focus on the concepts first, the actual programming second. This is 
#       a statistics course!
#   ii) Read the documentation for functions in case you're stuck. Googling is 
#       always a splendid option.

import numpy as np # numpy is the foundation for everything we'll do. 
import seaborn as sns 
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 666)
# This is a random number generator. We will pass it around to make the code
# reproducible. When you run you this code on your computer, your results 
# should match mine exactly, even though we are dealing with random numbers.

# simulate n = 10 throws of a die.
n = 10
values = rng.integers(low = 1, high = 6 + 1, size = n)

# Now let's simulate 100,000 throws.
n = 10 ** 5
values = rng.integers(low = 1, high = 6 + 1, size = n)

# Let's count the number of 1s, 2s, 3s, et cetera.
uniques, counts = np.unique(values, return_counts = True)

# uniques, counts = (a, b) 
# Equivalent to:
# uniques = a
# counts = b

# What should "counts" be? P(X = i) = 1/6 approx. 0.16666....
print(counts / n)

# Let's plot them too!
plt.bar(uniques, counts / n, align = 'center')
plt.show()

# Time to do something a little more interesting!
# What is the probability that the minimal die is 3 when 5 dice are cast?
# Let's walk through it!

# First simulate one throw of five dice:
n = 5
values = rng.integers(low = 1, high = 6 + 1, size = n)

# Then take the minimum of these.
np.min(values)

# Now do this several times.
n_reps = 1000 # Let's do it n_reps times first
throws = rng.integers(
    low = 1, 
    high = 6 + 1, 
    size = (n_reps, n))

# Size: (number of rows, number of columns), R x C, think "RC cars"

# Now we need to take the minimum of each row!

def f(x):
    return np.max(x) - np.min(x)

minimums = np.apply_along_axis(
    func1d = f, 
    axis = 1, 
    arr = throws)

minimums = np.apply_along_axis(
    func1d = lambda x: np.max(x) - np.min(x), 
    axis = 1, 
    arr = throws)

# Again, we must collect the values of the throws.
uniques, counts = np.unique(minimums, return_counts = True)

# Use docstrings to document your functions https://bit.ly/35RTWCp
def product_throw(throws, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "face" is the face of the die and "probability"
    is the approximate probability that said face is the minimal die after
    "throws" throws of the dice.

    n_reps is the number of repetitions used in the simulation.
    """
    results = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    minimums = np.apply_along_axis(func1d = np.prod, axis = 1, arr = results)
    uniques, counts  = np.unique(minimums, return_counts = True)
    return {"face" : uniques, "probability" : counts / n_reps}


# What does this function do?
help(minimum_throw)

# Let's simulate and plot!
simulated_throws = prod_throw(5, rng = rng)
face = simulated_throws["face"]
probabilities = simulated_throws["probability"]
np.sum([face[i] * probabilities[i] for i in range(0, len(probabilities))])

np.sum(face * probabilities)

a = list(range(0, len(probabilities)))
for i in range(0, len(probabilities)):
    a[i] = face[i] * probabilities[i]
np.sum(a)

sns.barplot(
    x = "face", 
    y = "probability", 
    data = simulated_throws)
plt.show()

simulated_throws["probability"][3]

# Tasks: 
# (1) Write a function maximum_throw that approximates the probability of the 
#     maximal throw. It should take the same arguments as 'minimum_throw'. 
#     Remember to write an appropriate docstring. Plot a bargraph of 
#     maximum_throw alongside a  bargraph for minimum_throw when `throw = 5` 
#     in both cases. What do you see?
# (2) Write a function sum_throw that finds the probability of obtaining every 
#     possible sums of `throw` dice. Make a barplot of the distribution when
#     `throw` equals 7.
# (3) Write a function that calculates the expected value of the sums in (2), 
#     i.e, sum(probs * value). Remember the docstring.
# (4) Write a function that finds the probability of obtaining every possible
#     product of `throw` dice. Rember the docstring. Find the probability 
#     that the product of 5 dice throws exceeds 3888. 
#
# Hints: Look up np.max, np.sum. 
