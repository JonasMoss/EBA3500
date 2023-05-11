import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt

mod = smf.quantreg("y ~ x", data = pd.DataFrame([y, x]).T)
res_lad = mod.fit(q = 0.5)
res_lad.params 

plt.scatter(x, y)
plt.plot(x, res_lad.params[0] + x * res_lad.params[1], color = "black")
plt.show()

