# rsq prototype 2
import numpy as np
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 1, num = 100)
y = np.exp(3 * x ** 2) + rng.uniform(-1, 1, 100)

res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
lower = np.sum((y - np.mean(y)) ** 2) 
upper = np.sum((y - (res_ls.params[0] + x * res_ls.params[1])) ** 2) 
lower - upper # 1421.4833888194755
1 - upper / lower # 0.6554432151711667
res_ls.rsquared # 0.6554432151711667
np.corrcoef(x, y)[0, 1]**2 # 0.6554432151711672

np.mean(y) # 4.304984335161987
plt.scatter(x, y)
plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "red")
plt.plot(x, np.mean(y) + 0 * x , color = "black")
plt.show()

# rsq prototype 1
import numpy as np
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 1, num = 100)
y = 2 + 3 * x + rng.uniform(-1, 1, 100)

res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res_lad = smf.quantreg("y ~ x", data = pd.DataFrame([y, x]).T).fit(q = 0.5)

lower = np.sum(abs(y - np.median(y)))
upper = np.sum(abs(y - (res_lad.params[0] + x * res_lad.params[1])))
1 - upper / lower # 0.4282332871090164
res_ls.rsquared # 0.6888118053315937

plt.scatter(x, y)
plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "red")
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.plot(x, np.mean(y) + 0 * x , color = "black")
plt.plot(x, np.median(y) + 0 * x , color = "blue")
plt.show()
