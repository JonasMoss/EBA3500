import numpy as np

import statsmodels.api as sm

import statsmodels.formula.api as smf

dat = sm.datasets.get_rdataset("Guerry", "HistData").data

results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

x = np.random.random(100)
u = np.random.random(100)
y = 2 + x + u


nsample = 100
x = np.linspace(0, 10, 100)
X = np.column_stack((x, x**2))
beta = np.array([1, 0.1, 10])
e = np.random.normal(size=nsample)

X = sm.add_constant(X)
y = np.dot(X, beta) + e

X @ beta