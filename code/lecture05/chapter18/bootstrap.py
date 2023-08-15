import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

egypt = pd.read_csv("egypt.csv")
egypt.head()

sns.kdeplot(egypt.age)
plt.show()
plt.clf()


egypt.age.mean()

n_reps = 1000
boots = egypt.age.sample(n=egypt.age.size * n_reps, replace=True)
boot_means = boots.to_numpy().reshape((egypt.age.size, n_reps)).mean(axis=0)

plt.hist(boot_means)
plt.show()
