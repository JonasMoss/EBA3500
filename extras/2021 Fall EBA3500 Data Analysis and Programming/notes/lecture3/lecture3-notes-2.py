import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd

n_reps = 10000


# Simulation.
pvalues = np.zeros(n_reps)
num = 20

for i in range(n_reps):
    # Simulat stuffe.
    x = np.linspace(0, 1, num)
    u = rng.normal(0, np.sqrt(res_ls.scale), num)
    y = res_ls.params[0] + 0 * x + u

    # Fit
    res_sim = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
    pvalues[i] = res_sim.pvalues[1]

plt.hist(pvalues, density = True)
plt.show()

# p-value
res = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res.summary()


# Simulation 2.
n_reps = 10000
pvalues = np.zeros(n_reps)
num = 20

for i in range(n_reps):
    # Simulat stuff.
    x = np.linspace(0, 1, num)
    u = rng.normal(0, np.sqrt(res_ls.scale), num)
    y = res_ls.params[0] + res_ls.params[1] * x + u

    # Fit
    res_sim = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
    pvalues[i] = res_sim.pvalues[1]

plt.hist(pvalues, density = True)
plt.show()