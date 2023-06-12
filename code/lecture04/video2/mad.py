import numpy as np

old_faithful = np.loadtxt("old_faithful.dat", dtype=np.float64)

x = old_faithful


def mad(x):
    median = np.median(x)
    return np.median(np.abs(median - x))
