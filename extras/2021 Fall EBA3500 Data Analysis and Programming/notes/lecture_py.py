### Example of the CLT:
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

## Simulate the exponential
rng = np.random.default_rng(seed = 313)
n_reps = 10 ** 4
n = 30
x = rng.exponential(size = (n_reps, n))
means = np.apply_along_axis(np.mean, 1, x)
sns.histplot(means, stat = "density")
plt.show()

## Plot the histogram along with a normal density.
xx = np.linspace(0, 3, 1000)
sns.histplot(means, stat = "density")
plt.plot(xx, stats.norm.pdf(xx, 1, 1/np.sqrt(n)), color = "black")
plt.show()

## Simulate the median
n_reps = 10 ** 4
n = 100
x = rng.exponential(size = (n_reps, n))
medians = np.apply_along_axis(np.median, 1, x)
sns.histplot(medians, stat = "density")
plt.plot(xx, stats.norm.pdf(xx, np.mean(medians), np.std(medians)), color = "black")
plt.show()

## Difference between n^(1/2) and n^(1/3).
n = np.arange(0, 10000) + 1
plt.plot(n, 1 / n ** (1/2))
plt.plot(n, 1 / n ** (1/3))
plt.show()

## Exponential mean CI
def ci(x):
    n = len(x)
    z_q = stats.norm.ppf(1 - 0.05 / 2)
    lower = np.mean(x) - z_q/np.sqrt(n)
    upper = np.mean(x) + z_q/np.sqrt(n)
    return [lower, upper]

ci(x[1:])
cis = np.apply_along_axis(ci, 1, x)
coverages = np.apply_along_axis(lambda x: x[0] < 1 < x[1], 1, cis)
np.mean(coverages)