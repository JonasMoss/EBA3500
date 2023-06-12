import numpy as np
import scipy.stats as sps

n = 100
eps = 0.5
gamma = sps.gamma(n, scale = 1/n)
mean, var, skew, kurt = gamma.stats(moments='mvsk')

def deviation(n, eps):
    