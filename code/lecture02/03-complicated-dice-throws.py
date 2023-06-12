import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=666)

# Now let's simulate 100,000 throws.
n = 10**5
values = rng.integers(low=1, high=6 + 1, size=n)

# Let's count the number of 1s, 2s, 3s, et cetera.
uniques, counts = np.unique(values, return_counts=True)
