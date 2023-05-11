import numpy as np

A = np.array([[1, 0, 1], 
[0, 1, 0], 
[1, 0, 1]])

np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eigvals(A)

np.transpose(A)
import numpy as np
from scipy.optimize import minimize

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

plt.rc("figure", figsize=(16,8))
plt.rc("font", size=14)

data = sm.datasets.engel.load_pandas().data
data.head()

mod = smf.quantreg("foodexp ~ income", data)
res = mod.fit(q=0.5)
mod = smf.ols("foodexp ~ income", data)
res = mod.fit()
print(res.summary())
fig = sm.graphics.plot_fit(res, 1)
fig.tight_layout(pad=1.0)
plt.show()
