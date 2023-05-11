# Prototype 1
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed = 313)

x = np.linspace(0, 1, num = 100)
y = 2 + 3 * x + rng.uniform(-1, 1, 100)

plt.scatter(x, y)
plt.plot(x, 2 + 3 * x, color = "black")
plt.show()



# Prototype 2
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed = 313)

x = np.linspace(0, 1, num = 100)
y = np.exp(3 * x ** 2) + rng.uniform(-1, 1, 100)

plt.scatter(x, y)
plt.plot(x, np.exp(3 * x ** 2), color = "black")
plt.show()


import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

mod = smf.quantreg("y ~ x", data = pd.DataFrame([y, x]).T)
res_lad = mod.fit(q = 0.5)
res_lad.params 

plt.scatter(x, y)
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.show()


import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

res_ls = smf.ols("y ~ x", data = pd.DataFrame([y, x]).T).fit()
res_ls.params 

plt.scatter(x, y)
#plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "black")
plt.show()

plt.scatter(x, y)
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.plot(x, res_ls.params[0] + x * res_ls.params[1], color = "red")
plt.show()

# The linear model
rng = np.random.default_rng(seed = 313)

x = np.linspace(0, 1, num = 100)
y = 2 + 3 * x + rng.uniform(-1, 1, 100)

mod = smf.quantreg("y ~ x", data = pd.DataFrame([y, x]).T)
res_lad = mod.fit(q = 0.5)

plt.scatter(x, y)
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.show()

res_lad.params 


# Example

from rdatasets import data

mtcars = data("mtcars")
mtcars.head()

res_lad = smf.quantreg("mpg ~ wt", data = mtcars).fit(q = 0.5)
res_ls = smf.ols("mpg ~ wt", data = mtcars).fit()

plt.scatter(mtcars["wt"], mtcars["mpg"])
plt.plot(mtcars["wt"], res_lad.params[0] + mtcars["wt"] * res_lad.params[1], color = "black")
plt.plot(mtcars["wt"], res_ls.params[0] + mtcars["wt"] * res_ls.params[1], color = "red")
plt.show()

res_lad.params 
res_ls.params 
