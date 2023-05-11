import numpy as np

np.median([1, 2, 2, 3]) 
np.array([1, 2, 3]) * 2 
np.ones(10)

def mean_throw(throws, rng, n_reps = 10 ** 5):
    results = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    means = np.apply_along_axis(func1d = np.mean, axis = 1, arr = results)
    uniques, counts = np.unique(means, return_counts = True)
    return {"sum": uniques, "probability": counts / n_reps}



np.array([1, 2, 3]) * np.array([2, 3, 4])

def fun(x):     
    for i in range(len(x) - 1):          						
        x[i + 1] = x[i + 1] * x[i]      	
    return(x)

def fun(n):
    x = np.zeros(n)
    x[0] = 1
    for i in range(n - 1):
        x[i + 1] = 1 + x[i]
    return(x)
rng = np.random.default_rng(seed = 313)
fun(10)

np.random.default_rng(seed = 313).random(10)

[1, 2, 3] * [1, 2, 3]
np.array([1, 2, 3]) * [1, 2, 3]


import numpy as np
n_reps = 10 ** 5
n = 100
rng = np.random.default_rng(seed = 313)

def fun(x):     
	for i in range(len(x) - 1):         
		x[i + 1] = x[i + 1] * x[i]     
	return(x)


def sum_throw(throws, rng, n_reps = 10 ** 5):
    results = rng.integers(low = 1, high = 6 + 1, size = (n_reps, throws))
    maximums = np.apply_along_axis(func1d = np.sum, axis = 1, arr = results)
    uniques, counts = np.unique(maximums, return_counts = True)
    return {"sum" : uniques, "probability" : counts / n_reps}    