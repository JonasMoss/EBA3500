# Prototype 1
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd
rng = np.random.default_rng(seed = 313)

x = np.linspace(0, 1, num = 100)
u = rng.uniform(-33, 33, 100)
y = 2 + 3 * x + u

res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res_ls.params 

y = 2 + 3*x + np.sin(x*5*np.pi) * rng.uniform(0, 1, 100)
plt.scatter(x, y)
#plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "black")
plt.show()


### Exp

x = np.linspace(0, 1, num = 100)
u = rng.uniform(-np.exp(-3*x), np.exp(-3*x), 100)
y = np.exp(3 * x ** 2) + u

res_lad = smf.quantreg("y ~ x", data = pd.DataFrame([y, x]).T).fit(q = 0.5)
res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()

plt.scatter(x, y)
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "red")
plt.show()

## Haha


from rdatasets import data

acme = data("boot", "acme")
ducks = data("boot", "ducks")
ducks = data("boot", "ducks")

res_lad = smf.quantreg("plumage ~ behaviour", data = ducks).fit(q = 0.5)
res_ls = smf.ols("plumage ~ behaviour", data = ducks).fit()

plt.scatter(ducks.behaviour, ducks.plumage)
plt.plot(ducks.behaviour, res_lad.params[0] + ducks.behaviour * res_lad.params[1], color = "black")
plt.plot(ducks.behaviour, res_ls.params[0] + ducks.behaviour * res_ls.params[1], color = "red")
plt.show()
