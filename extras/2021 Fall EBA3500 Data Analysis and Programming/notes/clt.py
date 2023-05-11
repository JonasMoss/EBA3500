import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(seed = 313)

n_reps = 10 ** 4
n = 30
x = rng.exponential(size = (n_reps, n))
means = np.apply_along_axis(np.mean, 1, x)
sns.histplot(means, stat = "frequency")
plt.show()

## 
xx = np.linspace(0, 3, 1000)
sns.histplot(means, stat = "density")
plt.plot(xx, stats.norm.pdf(xx, 1, 1/np.sqrt(n)), color = "black")
plt.show()


medians = np.apply_along_axis(np.median, 1, x)
xx = np.linspace(0, 3, 1000)
sns.histplot(medians, stat = "density")
plt.plot(xx, stats.norm.pdf(xx, np.mean(medians), np.std(medians)), color = "black")
plt.show()