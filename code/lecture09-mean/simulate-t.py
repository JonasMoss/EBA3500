import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

# Using Gamma distribution? Hmm, this might not be the right place?
rng = np.random.default_rng(seed=313)
x = rng.gamma(1 / 2, 2, size=(100, 10000)).mean(axis=0)
mean = np.mean(x)
sd = np.std(x)


sns.kdeplot(x)
y = np.linspace(mean - 3 * sd, mean + 3 * sd, 100)
plt.plot(y, st.norm.pdf(y, mean, sd), color="red")
plt.show()
