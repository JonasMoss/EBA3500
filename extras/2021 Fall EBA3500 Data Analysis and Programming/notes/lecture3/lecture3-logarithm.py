# Illustration
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0, 10, num = 100)
y = np.log(x)

plt.plot(x, x, color = "black")
plt.plot(x, y, color = "black")
plt.show()

# Toy model
rng = np.random.default_rng(seed = 313)
x = np.linspace(0, 1, num = 100)
u = rng.uniform(-1, 1, 100)
y = np.exp(1 + 2 * x + u)

func = lambda x, a, b: np.exp(a + b * x)
param = curve_fit(func, x, y)[0]
param
res_ls = smf.ols("np.log(y) ~ x", data = pd.DataFrame([y, x]).T).fit()
res_ls.params 

plt.scatter(x, y)
plt.plot(x, func(x, 1, 2), color = "black")
plt.plot(x, func(x, *param), color = "red")
plt.show()

lower = np.sum((y - np.mean(y)) ** 2)
upper = np.sum((y - func(x, param[0], param[1])) ** 2)
1 - upper / lower
np.corrcoef(x, np.log(y))[1, 0] ** 2


# Illustration
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num = 100)
u = rng.uniform(-1, 1, 100)
y = np.exp(1 + 2 * x + u)

plt.scatter(x, np.log(y))
plt.plot(x, 1 + 2 * x)
plt.show()




# Interest
x = np.linspace(0, 50, num = 50)
u = rng.uniform(-0.1, 0.1, 50)
plt.scatter(x, 100 * 1.03 ** x * np.exp(u))
plt.plot(x, 100 * 1.03 ** x)
plt.show()
