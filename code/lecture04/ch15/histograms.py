import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

old_faithful = np.loadtxt("old_faithful.dat", dtype=np.float64)

plt.hist(old_faithful)
plt.show()
plt.clf()

plt.hist(old_faithful, density=True)
plt.show()
plt.clf()

sns.histplot(old_faithful)
plt.show()
plt.clf()


sns.histplot(old_faithful, kde=True)
plt.show()
plt.clf()

sns.histplot(old_faithful, stat="probability")
plt.show()
plt.clf()
