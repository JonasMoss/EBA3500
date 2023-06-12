import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Do some exploratory stuff.
# 2. Calculate gamma numerically.
# 3. Do a KS test.


egypt = pd.read_csv("egypt.csv")
sns.histplot(egypt.age, stat="density")
plt.show()

sns.histplot(egypt, x="age", stat="density", hue="sex", element="step")
plt.show()

sns.ecdfplot(egypt, x="age", hue="sex")
plt.show()

egypt.groupby(egypt.sex).agg(["mean", "std"])

sns.boxenplot(egypt, x="age", y="sex")
plt.show()
