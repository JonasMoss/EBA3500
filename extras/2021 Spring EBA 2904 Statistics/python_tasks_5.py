# Tasks for "Introduction to Numpy"

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## Task (i)
x = np.arange(1, 100 + 1) * 1.0
x.dtype
np.product(x)
x = np.arange(1, 10 + 1)
np.product(x)

## (ii) Calculate the sum of the 100 first squares! 1** 2 + 2**2 + ... 100**2
x = np.arange(1, 100 + 1) ** 2
np.sum(x) # 338350

## (iii) Find the variance of the first 100 squares!
x = np.arange(1, 100 + 1) ** 2
np.var(x)

## (iv) Approximate the minimum value of 5 * x ** 5 - 4 * x ** 3 + x on the 
## interval [-1,1]. (Hint: np.linspace and np.min).
## (v) Find the x where 5 * x ** 5 - 4 * x ** 3 + x attains its minimum. [Hint:
## np.argmin] (This is still on the interval [-1, 1]).

x = np.linspace(-1, 1, 100000)
y = 5 * x ** 5 - 4 * x ** 3 + x
np.min(y) # -2
np.argmin(y)
x[np.argmin(y)] # -1.0

## (vi) I want you to make a function f that calculates the sum of the n first
## reciprocal squares: f(n) = 1/1**2 + 1/2**2 + ... + 1/n**2. The plot the
## output of f when multiplied by 6 / pi ** 2. What happens? [Hint: (1/n)**2, not
## 1/n**2]. (Let n = 1 and 10 ** 5).

def f(n):
    """ Calculate the sum of the n first reciprocal squares."""
    x = np.arange(1, n + 1)
    return(np.sum((1 / x) ** 2))

def g(n):
    """ Calculate the sum of the n first reciprocal squares."""
    x = np.arange(1, n + 1)
    y = (1 / x) ** 2
    return(np.cumsum(y))

n = 10 ** 5
z = [f(i) for i in range(1, n + 1)]

plt.plot(np.arange(1, n + 1)[200:n], g(n)[200:n], color = "black")
plt.show()

plt.plot(np.arange(1, n + 1), g(n) * 6 / np.pi ** 2, color = "black")
plt.show()

# Sum of 1 / x** 2 converge to pi / 6 ** 2.
x = np.arange(1, 10 + 1)
y = np.cumsum(x)
