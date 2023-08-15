import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=313)
x = rng.normal(size=100)
mean = x.mean()
sd = x.std(ddof=1)


# https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales

supermarket = pd.read_csv("supermarket_sales.csv")
supermarket.head()

# cogs: Cost of good sold.
ecdf = ECDF(supermarket.cogs)
type(ecdf)
dir(ecdf)
ecdf.x
ecdf.y
plt.plot(ecdf.x, ecdf.y)
plt.show()

# Is there a difference between the cities?
set(supermarket.City)  # Find distinct cities.
np.unique(supermarket.City, return_counts=True)
# Mandalay, Naypyitaw, Yangon

plt.clf()
for city in set(supermarket.City):
    ecdf = ECDF(supermarket.query(f"City == '{city}'").cogs)
    plt.plot(ecdf.x, ecdf.y, label=city)

plt.legend(loc="upper left")
plt.show()

# Short exercise
# Go to the webpage https://seaborn.pydata.org/generated/seaborn.ecdfplot.html#seaborn.ecdfplot
# or google seaborn ecdfplot) and reproduce the analysis above.


# Are these distributions actually different?
from scipy.stats import kstest

mandalay = supermarket.query(f"City == 'Mandalay'").cogs
naypyitaw = supermarket.query(f"City == 'Naypyitaw'").cogs
yangon = supermarket.query(f"City == 'Yangon'").cogs
kstest(mandalay, naypyitaw).pvalue
kstest(mandalay, yangon).pvalue
kstest(naypyitaw, yangon).pvalue
