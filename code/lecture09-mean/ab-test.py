import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing

ccat = pd.read_csv("cookie_cats.csv")
ccat.head()
ccat.drop(ccat[ccat.sum_gamerounds == ccat.sum_gamerounds.max()].index, inplace=True)


x30 = ccat[ccat.version == "gate_30"].sum_gamerounds
x40 = ccat[ccat.version == "gate_40"].sum_gamerounds

ccat.drop(ccat[ccat.sum_gamerounds == ccat.sum_gamerounds.max()].index, inplace=True)
x30.max()
x40.max()

x30.std()
x40.std()

sns.kdeplot(ccat, x="sum_gamerounds", hue="version")
plt.show()

ccat["log_sum_gamerounds"] = np.log(ccat.sum_gamerounds + 1)


sns.kdeplot(ccat, x="log_sum_gamerounds", hue="version")
plt.show()

np.unique(x30, return_counts=True)


st.ttest_ind(x30, x40, equal_var=False)

r7_30 = ccat[ccat.version == "gate_30"].retention_7
r7_40 = ccat[ccat.version == "gate_40"].retention_7

r1_30 = ccat[ccat.version == "gate_30"].retention_1
r1_40 = ccat[ccat.version == "gate_40"].retention_1

st.ttest_ind(r7_30, r7_40, equal_var=False)
st.ttest_ind(r1_30, r1_40, equal_var=False)
