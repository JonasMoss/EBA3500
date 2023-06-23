# Sum up two lists
x = [1, 2, 3]
y = [5, 9, 4]
z = zip(x, y)
list(z)

z = [x + y for x, y in zip(x, y)]
z

import numpy as np

x = np.array([1, 2, 3])
y = np.array([5, 9, 4])
z = x + y
z
z.dtype
