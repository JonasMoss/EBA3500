import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

old_faithful = np.loadtxt("old_faithful.dat", dtype=np.float64)
sns.kdeplot(old_faithful)
sns.histplot(old_faithful, stat="density")
plt.show()
plt.clf()

# Exercise: Figure out how to modify the smoothing bandwidth
# parameter h multiplicatively.

sns.kdeplot(old_faithful, bw_adjust=0.01)
plt.show()
plt.clf()

# Point: The larger the smoothing bandwidth, the smoother the plot!

# Let's make our own kde-ish function.


# Also available in Scipy.
def standard_norm(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2)


def kde(x, h):
    """Returns the kernel density estimator of x with bandwidth h.
    The kernel is normal."""
    return lambda y: np.mean(standard_norm((y - x) / h) / h)


fun = kde(old_faithful, h=0.05)


def kde_np(x, h):
    """Returns the kernel density estimator of x with bandwidth h.
    The kernel is normal. Accepts numpy arrays as input."""
    return lambda y: [np.mean(standard_norm((z - x) / h)) / h for z in y]


fun = kde_np(old_faithful, h=20)
plt.plot(old_faithful, fun(old_faithful))
sns.kdeplot(old_faithful)
plt.show()
