import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

old_faithful = np.loadtxt("old_faithful.dat", dtype=np.float64)
sns.kdeplot(old_faithful)
plt.show()
plt.clf()

# Exercise: Figure out how to modify the smoothing parameter h.
