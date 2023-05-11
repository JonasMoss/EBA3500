import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)

def walker(n, func, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "result" is the result of applying "func" to a 
    random walk and "probability" is the probability of achieving that result.

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """

    bs = np.apply_along_axis(
        func1d = np.cumsum, 
        axis = 1, 
        arr = rng.integers(low = -1, high = 2, size = (n_reps, n)))
        
    results = np.apply_along_axis(func1d = func, axis = 1, arr = bs)     

    uniques, counts = np.unique(results, return_counts = True)
    return {"result" : uniques, "probability" : counts / n_reps}

def convolver(b):
    return np.max(np.convolve(b, np.repeat(1, 3), mode = 'valid'))

simulations = walker(1000, convolver, rng)
sns.barplot(
    x = "result", 
    y = "probability", 
    data = simulations)
plt.show()

# Task 2.
z = rng.integers(low = -1, high = 2, size = 100)
b = np.cumsum(z)
[b[0]] + list(np.diff(b))
[b[0]] + list(b[1:] - b[0:-1])
z

# Task 3.
result = simulations["result"]
probabilities = simulations["probability"]
e_z = np.sum(result * probabilities)
sd_z = np.sqrt(np.sum(result ** 2 * probabilities) - e_z ** 2)

# Task 4

# First makes a function that checks if a walk ever crosses 10.

def crosses_once(b):
    return np.max(b) > 10

# Then make a function that checks if a walk crosses 10 again, assuming it has
# crossed 10 once.

def crosses_twice(b):
    """ Returns True if the random walk crosses 10 again after having crossed
    10 once. """
    index = np.argmax(b == 11)
    if(index == len(b) - 1): return False
    return np.min(b[(index + 1):]) < 10

## Test it!
rng = np.random.default_rng(seed = 1)
n = 100
b = np.cumsum(rng.integers(low = -1, high = 2, size = n))
crosses_once(b)
crosses_twice(b)
graph = sns.scatterplot(x = range(1, n + 1), y = b)
graph.axhline(10)
plt.show()

def walker_filter(n, func, filter_func, rng, n_reps = 10 ** 5):
    """ 
    Returns a dictionary where "result" is the result of applying "func" to a 
    random walk and "probability" is the probability of achieving that result,
    provided "filter_func" is True.

    n_reps is the number of repetitions used in the simulation; rng is a 
    random number generator.
    """

    bs = np.apply_along_axis(
        func1d = np.cumsum, 
        axis = 1, 
        arr = rng.integers(low = -1, high = 2, size = (n_reps, n)))
        
    filtered_bs = bs[np.apply_along_axis(
        func1d = filter_func, 
        axis = 1, 
        arr = bs), ]

    results = np.apply_along_axis(
        func1d = func, 
        axis = 1, 
        arr = filtered_bs)     

    uniques, counts = np.unique(results, return_counts = True)
    return {"result" : uniques, "probability" : counts / len(filtered_bs)}

simulations = walker_filter(1000, crosses_twice, crosses_once, rng)