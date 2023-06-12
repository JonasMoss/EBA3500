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
a[:, 0]
a[:, 1]

# What is this?
a[:, :, 0]
a[:, :, 1]
a[:, :, 2]
