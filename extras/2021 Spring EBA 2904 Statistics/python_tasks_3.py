### ============================================================================
### Solutions to video 3 on histograms, densities, and the CLT.
### ============================================================================

import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(seed = 313)

# Task 1.
def clt(n, func, generator, n_reps, bins = "auto"):
    """ Simulates n values from generator n_reps times, applies func to the n
    values, then plots a histogram and normal density curve from the data."""
    x = generator((n_reps, n))
    y = np.apply_along_axis(
        func1d = func,
        axis = 1,
        arr = x
    )
    mean = np.mean(y)
    sd = np.std(y)
    xs = np.arange(mean - 3*sd, mean + 3*sd, 0.001)
    ax = sns.histplot(x = y, bins = bins, stat = "density")
    ax.plot(xs, stats.norm.pdf(xs, mean, sd), color = "black")
    plt.show()

clt(100, np.var, rng.standard_exponential, 10 ** 5)
clt(1000, np.var, rng.standard_exponential, 10 ** 5)

# Task 2

def f1(x):
    return np.sum(x ** 3)

clt(100, lambda x: np.sum(x ** 3), rng.standard_exponential, 10 ** 5)
clt(1000, lambda x: np.sum(x ** 3), rng.standard_exponential, 10 ** 5)
clt(100, lambda x: np.sum(np.exp(-x)), rng.standard_exponential, 10 ** 5)
clt(100, lambda x: np.median(x) - np.mean(x), rng.standard_exponential, 10 ** 5)
clt(100, lambda x: np.mean(abs(x) - np.median(x)), rng.standard_exponential, 10 ** 5)
clt(100, lambda x: np.sum(np.exp(-x)), rng.standard_normal, 10 ** 5)
clt(100, lambda x: np.median(x) - np.mean(x), rng.standard_normal, 10 ** 5)
clt(100, lambda x: np.mean(abs(x) - np.median(x)), rng.standard_normal, 10 ** 5)

# Task 3
clt(1000, np.min, rng.standard_exponential, 10 ** 5)
clt(1000, np.max, rng.standard_exponential, 10 ** 5)
clt(1000, np.min, rng.standard_normal, 10 ** 5)
clt(1000, np.max, rng.standard_normal, 10 ** 5)

# Task 4
clt(100, np.mean, rng.standard_cauchy, 10 ** 5, bins = 50)
