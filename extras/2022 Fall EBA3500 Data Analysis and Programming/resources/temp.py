import pyreadr
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm


endometrial = pyreadr.read_r("endometrial.Rda")["endometrial"]
mod = smf.logit("HG ~ NV + PI + EH", data = endometrial).fit()
mod.summary()

beta = mod.params
beta[0] = 10**5
beta[1] = 10**5
beta = [0, 2.332822e+07, 1.652592, 1.864493]

X = pd.concat([
  pd.Series(np.ones(endometrial.shape[0]), dtype = "int").rename('Intercept'), 
  endometrial], axis=1)
  
X0 = X.query("HG == 0")
X0 = X0.drop(columns = "HG")
X1 = X.query("HG == 1")
X1 = X1.drop(columns = "HG")
np.array(X0) @ np.transpose(beta)
np.array(X1) @ np.transpose(beta)


url = "https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"
bank = pd.read_csv(url)
bank.head()

mod = smf.logit("y ~ job + marital", data = bank).fit()
aov = sm.stats.anova_lm(mod, typ =1)



import numpy as np
import pandas as pd
liver = pd.read_csv("indian_liver_patient.csv")


import pyreadr
endometrial = pyreadr.read_r("endometrial.Rda")["endometrial"]

