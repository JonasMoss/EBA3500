import numpy as np

a = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[8, 9, 10, 11], [12, 13, 14, 15]],
        [[16, 17, 18, 19], [20, 21, 22, 23]],
    ]
)

# The first argument selects along the first axis.
a[0]
a[1]
a[2]

# The second along the second axis.
a[1, 0]
a[2, 1]

a[2, 1, 0]
a[2, 1][0]
a[2]
a[2][1, 0]
a[2, 1][0]

a[:, 0]
a[:, 1]

# What is this?
a[:, :, 0]
a[:, :, 1]
a[:, :, 2]

# Reshaping
a.shape
3 * 2 * 4
a.reshape(24)
a.flatten()
a.reshape((12, 2))
a.reshape((2, 2, 2, 3))

# Reversing
a.flatten()
np.flip(a.flatten())
np.flip(a)

# Views and steps
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
c[1:-1]
c[1:-2:2]
c[1::2]

# Boolean indexing
b = np.array([1, 2, 3, 4, 5])
b[b < 3]

# Automatic broadcasting!
a[a < 5]
