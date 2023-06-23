import numpy as np

a = np.array([[8, 1, 7, 4], [1, 2, 7, 5], [99, 1, 4, 2]])

a.min()
a.max()
a.sum()
a.size
a.mean()
a.sum() / a.size

# Functions can be used along axes!
a.min(axis=0)
a.min(axis=1)
a.sum(axis=1)

# Logical functions.
b = np.array([[1, 1, 2, 3], [1, 1, 2, 3], [1, 1, 1, 2]])

a == b
a > b
a >= b
(a >= b).all()
(a > 10).any()

# `argmax` functions

a.argmax()
a.reshape(12)
a.flatten()
a.flatten()[8]

np.unravel_index(8, a.shape)
a[2, 0]

a.argmin()

# Counts
a = [1, 2, 3, 2, 3, 1, 1, 1, 1, 2, 4, 6, 3, 6, 1, 1, 1, 2, 2, 3, 3, 4, 3, 3]

np.unique(np.array(a))
np.unique(np.array(a), return_counts=True)
