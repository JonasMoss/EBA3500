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
# Hints: Look up np.max, np.sum. Check out "expected value" on wikipedia if you have to.

import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)


### Task 1
def maximum_throw(throws, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "face" is the face of the die and "probability"
    is the approximate probability that said face is the maximal die after
    "throws" throws of the dice.

    n_reps is the number of repetitions used in the simulation.
    """
    results = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    maximums = np.apply_along_axis(func1d = np.max, axis = 1, arr = results)
    uniques, counts = np.unique(maximums, return_counts = True)
    return {"face" : uniques, "probability" : counts / n_reps}

def minimum_throw(throws, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "face" is the face of the die and "probability"
    is the approximate probability that said face is the minimal die after
    "throws" throws of the dice.

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """
    sims = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    results = np.apply_along_axis(func1d = np.min, axis = 1, arr = sims)
    uniques, counts = np.unique(results, return_counts = True)
    return {"face" : uniques, "probability" : counts / n_reps}

# Let's simulate and plot!
minimal_throws = minimum_throw(5, rng = rng)
maximal_throws = maximum_throw(5, rng = rng)

fig, ax = plt.subplots(1,2)
sns.barplot(x = "face", y = "probability", data = maximal_throws, ax = ax[0])
sns.barplot(x = "face", y = "probability", data = minimal_throws, ax = ax[1])
plt.show()

### Task 2

def sum_throw(throws, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "sum" is the sum of the dice and "probability"
    is the approximate probability that said sum occured.

    n_reps is the number of repetitions used in the simulation.
    """
    results = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    maximums = np.apply_along_axis(func1d = np.sum, axis = 1, arr = results)
    uniques, counts = np.unique(maximums, return_counts = True)
    return {"sum" : uniques, "probability" : counts / n_reps}

# Let's simulate and plot!
simulated_throws = sum_throw(7, rng = rng)
sns.barplot(
    x = "sum", 
    y = "probability", 
    data = simulated_throws)
plt.show()

### Task 3

def sum_expected(throws, rng, n_reps = 10 ** 5):
    """ 
    Approximates the expected value of sum of "throws" dice throws.

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """
    simulated_throws = sum_throw(throws, rng)
    sums = simulated_throws["sum"]
    probabilities = simulated_throws["probability"]
    return np.sum(sums * probabilities)

# Let's plot the expected values, checking the linearity of expectation, i.e,
# E(sum(X_i)) = sum(E(X_i)). When every X_i is indepent of each other, we'll
# have E(sum(X_i)) = n E(X_1) when we sum over n iterations. 

xs = range(1, 17)
ys = [sum_expected(throws, rng) for throws in xs]
sns.scatterplot(x = xs, y = ys) # Expects the function y = a*x for some a!
plt.show()

### Task 4

def product_throw(throws, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "product" is the product of "throws" throws and 
    "probability" is the approximate probability that the product equals 
    "product".

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """
    sims = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    results = np.apply_along_axis(func1d = np.product, axis = 1, arr = sims)    
    uniques, counts = np.unique(results, return_counts = True)
    return {"product" : uniques, "probability" : counts / n_reps}

simulated_throws = product_throw(5, rng)
# The probability that the product exceeds 3888:
products = simulated_throws["product"]
probabilities = simulated_throws["probability"]
sum([probabilities[i] for i, _ in enumerate(products) if products[i] > 3888])

### Coda: Always a good idea to generalize your functions!

def throw_dice(throws, func, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "result" is the result of applying func to 
    "throws" throws and "probability" is the approximate probability that the 
    result equals "result".

    n_reps is the number of repetitions used in the simulation.
    """
    
    simulation = rng.integers(low = 1, high = 7, size = (n_reps, throws))
    result = np.apply_along_axis(func1d = func, axis = 1, arr = simulation)    
    uniques, counts = np.unique(products, return_counts = True)
    return {"result" : uniques, "probability" : counts / n_reps}
