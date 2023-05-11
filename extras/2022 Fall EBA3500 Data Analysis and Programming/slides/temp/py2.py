import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 3, 100)
trues = np.sin(2 * np.pi * x) * x * np.exp(x)
y = trues + rng.normal(0, 3, 100)

import statsmodels.formula.api as smf
def fit_model(deg):
  formula = "y ~ np.vander(x, " + str(deg) + ", increasing = True)-1"
  return smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
  
fit_model(5).aic
fit_model(7).aic


[(deg, fit_model(deg).aic) for deg in range(2, 16)]

plt.clf()
plt.plot(x, trues, color = "black", linewidth=0.5)
plt.scatter(x, y, s = 0.1, color = "black")
plt.ylim(-50, 25)

for deg in [5, 7, 13, 18]:
  formula = "y ~ np.vander(x, " + str(deg) + ", increasing = True)-1"
  model = smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
  plt.plot(x, model.predict())
  
plt.legend(["true", "data", 5, 7, 13, 18])

plt.show()
plt.clf()

