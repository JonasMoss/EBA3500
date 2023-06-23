import numpy as np

a = np.array([[1, 2], [3, 4]])
a.ndim
a.size
a.shape

b = np.array([[1, 2], [3, 4], [5, 6]])
b.shape  # row then columns. RC Cars.
b.ndim
b.size

c = np.array([[[1, 2], [2, 3]], [[4, 5], [7, 9]]])
c.size
c.ndim
c.shape

c.reshape((4, 1))
c.reshape(8)
