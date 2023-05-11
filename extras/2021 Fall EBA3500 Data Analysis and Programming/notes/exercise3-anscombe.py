# rsq prototype 2
import numpy as np
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
# rsq_lad

def rsq_lad(x, y):
    res = smf.quantreg("y ~ x", data = pd.DataFrame({'y':y, 'x': x})).fit(q = 0.5)
    lower = np.sum(np.abs(y - np.median(y))) 
    upper = np.sum(np.abs(y - (res.params[0] + x * res.params[1])))
    return np.max([(1 - upper / lower), 0])

import seaborn as sns 

sns.set_theme(style="ticks")

df = sns.load_dataset("anscombe")

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2, ci = None, palette = "muted", height = 4, scatter_kws = {"s": 50, "alpha": 1})
plt.show()

sns.lmplot(x="y", y="x", col="dataset", hue="dataset", data=df, col_wrap=2, ci = None, palette = "muted", height = 4, scatter_kws = {"s": 50, "alpha": 1})
plt.show()

df.groupby("dataset").apply(lambda z: rsq_lad(z["x"], z["y"]))
df.groupby("dataset").apply(lambda z: rsq_lad(z["y"], z["x"]))


import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 1, num = 100)
v = rng.uniform(-1, 1, 100)
u = np.exp(3 * x ** 2) - (2 + 3 * x) + v
y = 2 + 3 * x + u



## Lad correlation
def corr_lad(x, y):
    res = smf.quantreg("y ~ x", data = pd.DataFrame({'y':y, 'x': x})).fit(q = 0.5)
    lower = np.sum(np.abs(y - np.median(y))) 
    upper = np.sum(np.abs(y - (res.params[0] + x * res.params[1])))
    return np.sign(res.params[1]) * np.max([(1 - upper / lower), 0])



