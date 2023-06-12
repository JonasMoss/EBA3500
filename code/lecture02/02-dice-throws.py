import numpy as np

rng = np.random.default_rng(seed = 313)
throws = rng.integers(1, 7, size = (10000, 2))
# throws contaisn 10000 rows of two dice throws.
totals = throws.sum(axis = 1)
maxs = throws.max(axis = 1)
totals
maxs

totals == 7
maxs == 6

x = np.logical_or(totals == 7, maxs == 6)
x

x.mean()

def prob(rng, n_reps = 10000):
  throws = rng.integers(1, 7, size = (10000, 2))
  return np.logical_or(throws.sum(axis = 1) == 7, throws.max(axis = 1) == 6).mean()
  
prob(rng)

rng = np.random.default_rng(seed = 313)
prob(rng)