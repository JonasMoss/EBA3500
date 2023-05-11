import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed = 313)

x = np.linspace(0, 1, num = 100)
u = np.exp(3 * x ** 2) - (2 + 3 * x) + rng.uniform(-1, 1, 100)
y = 2 + 3 * x + u


import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed = 313)

num = 20
x = np.linspace(0, 1, num = 20)
u = rng.uniform(-1, 1, 20)
y = 2 + 0 * x + u

plt.scatter(x, y)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd
res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res_ls.params 
plt.scatter(x, y)
plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "black")
plt.show()
res_ls.params 


# p-value
res = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res.summary()