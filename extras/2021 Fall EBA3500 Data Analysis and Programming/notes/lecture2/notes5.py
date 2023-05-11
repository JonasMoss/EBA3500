# Prototype 1
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd
from scipy.optimize import curve_fit

rng = np.random.default_rng(seed = 313)
x = sort(np.linspace(0, 1, num = 100))
u = rng.uniform(-1, 1, 100)
y1 = 2 + 3 * x + u
y2 = np.exp(3 * x ** 2) + u

func = lambda x, a, b: np.exp(a * x ** b)

param1 = curve_fit(func, x, y1)[0]
param2 = curve_fit(func, x, y2)[0]

def rsq(x, y):
    params = curve_fit(func, x, y)[0]
    lower = np.mean((np.mean(y) - y) ** 2)
    upper = np.mean((func(x, params[0], params[1]) - y) ** 2)
    return 1 - upper / lower

plt.scatter(x, y1)
plt.plot(x, func(x, param1[0], param1[1]), color = "black")
plt.show()

plt.scatter(x, y2)
plt.plot(x, func(x, param2[0], param2[1]), color = "black")
plt.show()

rsq(x, y1)
rsq(x, y2)

def nls_plotter(y, x, func):
    params = curve_fit(func, x, y)[0]
    lower = np.mean((np.mean(y) - y) ** 2)
    upper = np.mean((func(x, *params) - y) ** 2)
    plt.scatter(x, y)
    plt.plot(x, func(x, *params), color = "black")
    plt.show()
    return {"rsq": 1 - upper / lower, "params" : params}



nls_plotter(y2, x, lambda x, a, b, c: a * x ** 2 + b * x ** c)

