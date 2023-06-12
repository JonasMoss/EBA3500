import numpy as np

a = [1, 2, 3, 2, 3, 1, 1, 1, 1, 2, 4, 6, 3, 6, 1, 1, 1, 2, 2, 3, 3, 4, 3, 3]

np.unique(np.array(a))
np.unique(np.array(a), return_counts=True)
