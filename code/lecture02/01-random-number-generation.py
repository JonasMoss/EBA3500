import numpy as np

rng = np.random.default_rng(seed=313)
rng

rng.uniform(0, 1, size=10)

rng.uniform(0, 1, size=(2, 10))

rng1 = np.random.default_rng(seed=313)
rng2 = np.random.default_rng(seed=313)

rng1.uniform(0, 1, size=(2, 2))
rng2.uniform(0, 1, size=(2, 2))

rng1 = np.random.default_rng()
rng2 = np.random.default_rng()
rng1.uniform(0, 1, size=(2, 2))
rng2.uniform(0, 1, size=(2, 2))

rng1 = np.random.default_rng(seed=313)
rng2 = np.random.default_rng(seed=313)
x = rng1.uniform(2, 5, size=(2, 2))  # starting at 2 and ending at 5,
y = rng2.uniform(0, 1, size=(2, 2))  # starting at 0 and ending at 1.

x
3 * y + 2

# Generate an array of uniformly distributed numbers on $[1,5]$ with 
# $3$ rows and $4$ columns.
