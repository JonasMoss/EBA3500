import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
import seaborn as sns

### ============================================================================
### Step 1: Important and visualize, crudely.
### ============================================================================

description = "This dataset has a binary response (outcome, dependent) variable called admit. There are three predictor variables: gre, gpa and rank. We will treat the variables gre and gpa as continuous. The variable rank takes on the values 1 through 4. Institutions with a rank of 1 have the highest prestige, while those with a rank of 4 have the lowest. We can get basic descriptives for the entire data set by using summary. To get the standard deviations, we use sapply to apply the sd function to each variable in the dataset."

admission = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
pd.head(admission[1:6])

sns.pairplot(admission)
plt.show()
np.corrcoef(np.asarray(admission.T)) 

# We decide to look at gre!
sns.lmplot(x="gre", y="admit", col = "rank", data=admission, y_jitter = .03)
plt.show()

### ============================================================================
### Step 2: Show the linear regression line may be bad!
### ============================================================================

x = np.linspace(0, 1, 11)
y = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1])
sns.lmplot(x="x", y="y", data=pd.DataFrame({'x':x, 'y':y}))
plt.show()

### ============================================================================
### Step 3: What do we do? Search google for "curve between 0 and 1"
### ============================================================================

logistic = lambda x: 1/(1 + np.exp(-x))
x_ = np.linspace(-6, 6, 100)
plt.plot(x_, logistic(x_))
plt.show()

### ============================================================================
### Step 4: Use this function in curve_fit!
### ============================================================================
from scipy.optimize import curve_fit
func = lambda x, a, b: logistic(a + b * x)
param = curve_fit(func, x, y)[0]

plt.scatter(x, y)
x_ = np.linspace(0, 1, 100)
plt.plot(x_, func(x_, param[0], param[1]), color = "red")
plt.show()

### ============================================================================
### Step 5: May use any cumulative distribution function!
### ============================================================================
from scipy import stats

source = https://docs.scipy.org/doc/scipy/reference/stats.html

func_norm = lambda x, a, b: stats.norm.cdf(a + b * x)
param_norm = curve_fit(func_norm, x, y)[0]

plt.scatter(x, y)
x_ = np.linspace(0, 1, 100)
plt.plot(x_, func_norm(x_, param_norm[0], param_norm[1]), color = "red")
plt.plot(x_, func(x_, param[0], param[1]), color = "blue")
plt.show()



### ============================================================================
### Step 6: Go back to the GRE problem
### ============================================================================

func_logit = func
x = admission["gre"].values
y = admission["admit"].values
param_logit = curve_fit(func_logit, (x - np.mean(x)) / np.std(x), y)[0]
param_norm = curve_fit(func_norm, (x - np.mean(x)) / np.std(x), y)[0]

sns.scatterplot(x = "gre", y = "admit", data = admission, y_jitter = 0.03)
x_ = np.linspace(min(x), max(x), 100)
plt.plot(x_, func_norm((x_ - np.mean(x_)) / np.std(x_), param_norm[0], param_norm[1]), color = "red")
plt.plot(x_, func((x_ - np.mean(x_)) / np.std(x_), param_logit[0], param_logit[1]), color = "blue")
plt.show()

### ============================================================================
### Step 7: !! But this is not how it's usually done !!
### ============================================================================




plt.scatter(admission["gre"], admission["admit"], color = "black")
plt.show()

# Regplot
sns.regplot(x="gpa", y="admit", data=admission, y_jitter = .03)
plt.show()

# Regplot
sns.regplot(x="gpa", y="admit", col = "rank", hue = "gre", data=admission,
    y_jitter = .03, logistic = True)
plt.show()

# Logistic regplot
f, ax = plt.subplots(figsize=(5, 6))


sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03);


fit_ls = smf.ols("admit ~ gre", data = admission).fit()
plt.scatter(admission["gre"], admission["admit"], color = "black")
plt.plot()
plt.show()

#### Check check check
sns.lmplot(x="gpa", y="admit", col = "rank", hue = "gre", data=admission,
    y_jitter = .03, logistic = True)
plt.show()

sns.lmplot(x="gpa", y="admit", col = "rank", data=admission, y_jitter = .03)
plt.show()

sns.lmplot(x="gre", y="admit", col = "rank", data=admission, y_jitter = .03)
plt.show()

sns.pairplot(admission)

###

smf.logit("admit ~ gre", data = admission)

smf.probit("admit ~ gre", data = admission)

probit_fit = smf.probit("admit ~ gre", data = admission).fit()
logit_fit = smf.logit("admit ~ gre", data = admission).fit()

def rsq_mcfadden(fit):
    lower = fit.llnull
    upper = fit.llf
    1 - upper / lower


