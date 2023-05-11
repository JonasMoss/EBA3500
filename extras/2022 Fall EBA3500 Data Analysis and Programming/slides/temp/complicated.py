import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd
rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 3, 100)
trues = np.sin(2 * np.pi * x) * x * np.exp(x)
y = trues + rng.normal(0, 3, 100)
plt.plot(x,trues, color = "red")
plt.scatter(x, y)
plt.show()
plt.clf()

formula = "outcome ~ np.vander(prediction, 7, increasing=True) - 1"

for deg in range(3, 15):
  plt.cla()
  formula = "y ~ np.vander(x, " + str(deg) + ", increasing = True)-1"
  model = smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
  plt.plot(x, model.predict())
  plt.ylim(-50, 25)
  plt.title("deg = " + str(deg))
  plt.scatter(x, y, s = 0.1, color = "black")
  plt.plot(x, trues, color = "red", linewidth=0.5)
  plt.savefig("fig"+str(deg)+".png")
  plt.pause(0.2)

plt.show()
plt.clf()

z = 1 * (trues > 0)

for df in range(3, 15):
  plt.cla()
  formula = "y ~ bs(x, degree = 3, " + "df = " + str(df) + ")"
  model = smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
  plt.plot(x, model.predict())
  plt.ylim(-50, 25)
  plt.title("df = " + str(df))
  plt.scatter(x, y, s = 0.1, color = "black")
  plt.plot(x, trues, color = "red", linewidth=0.5)
  plt.pause(0.2)

plt.show()
plt.clf()


formula = "y ~ bs(x, degree = 3" + "df = " + str(df) + ")"
model = smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
plt.plot(x, model.predict())
plt.plot(x, trues, color = "red", linewidth=0.5)
plt.pause(0.01)




z = 1 * (trues > 0)

def fit_model(df):
  formula = "z ~ bs(x, degree = 3, " + "df = " + str(df) + ")"
  return smf.logit(formula, data = pd.DataFrame({"x" :x, "z":z})).fit()

for df in range(3, 15):
  plt.cla()
  formula = "y ~ bs(x, degree = 3, " + "df = " + str(df) + ")"
  model = smf.ols(formula, data = pd.DataFrame({"x" :x, "y":y})).fit()
  plt.plot(x, model.predict())
  plt.ylim(-50, 25)
  plt.title("df = " + str(df))
  plt.scatter(x, y, s = 0.1, color = "black")
  plt.plot(x, trues, color = "red", linewidth=0.5)
  plt.pause(0.2)









