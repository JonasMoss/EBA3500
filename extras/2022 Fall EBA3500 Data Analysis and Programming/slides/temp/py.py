import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd

predictions = pd.read_csv("data/predictions.csv")
predictions = predictions.sort_values(by = "prediction")

formula = "outcome ~ prediction + I(prediction**2) + np.log(prediction) + I(prediction**3)"
formula = "outcome ~ np.vander(prediction, 7, increasing=True) - 1"
formula = "outcome ~ bs(prediction, degree = 3, df = 5)"

model = smf.logit(formula, data = predictions).fit()
plt.plot(predictions.prediction, model.predict())
plt.xlim(left=0, right=1)
plt.ylim(bottom=0, top=1)
plt.show()
plt.clf()






import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


admission = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
admission.head()
model = smf.logit("admit ~ gre + gpa + C(rank)", data = admission).fit()






X = add_constant(pd.DataFrame({x: np.linspace(0, 1, 300)}))
se = np.sqrt(np.array([y @ model.cov_params() @ y for y in np.array(X)]))
predictions = model.predict(X) 
df = pd.DataFrame({
  'x': X[x], 
  'y': predictions, 
  'ymin': expit(logit(predictions) - 1.96*se), 
  'ymax': expit(logit(predictions) + 1.96*se)})
  
  
def logistic(formula, x, data):
  model = smf.logit(formula, data = data).fit()
  X = model.model.exog
  preds = model.predict()
  F = lambda x: 1/(1+np.exp(-x))
  f = lambda x: np.exp(-x)/(1 + np.exp(-x)) ** 2
  g = lambda x: x @ model.cov_params() @ x * f(model.params @ x) ** 2
  taus_sqrt = np.sqrt(np.array([g(y) for y in np.array(X)]))
  hats = np.array([F(model.params @ y) for y in np.array(X)])
  df = pd.DataFrame({
    'x': np.array(data[x]), 
    'y': preds, 
    'ymin': hats - 1.96*taus_sqrt, 
    'ymax': hats + 1.96*taus_sqrt})
  ax = df.plot(x = 'x', y = 'y')
  ax.fill_between(x = df['x'], y1 = df['ymax'], y2 = df['ymin'], alpha=.2)
  ax.set_xlim(left=0, right=1)
  ax.set_ylim(bottom=0, top=1)
  ax.get_legend().remove()  
  
  
  
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import product # We'll see how this works below.
params = np.array(list(product([-1, 0 ,1], [-1,0,1])))
x = np.linspace(-3, 3, 100)
c = 1
f = lambda x, a, b, c: c + b * x + a * x ** 2
# Let's plot it now.
fig, axs = plt.subplots(3, 3)
for (a, b), (i, j) in zip(params, product(range(3), range(3))):
  axs[i, j].plot(x, f(x, a, b, c))
