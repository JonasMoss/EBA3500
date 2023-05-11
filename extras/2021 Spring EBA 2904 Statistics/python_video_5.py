# An introduction to numpy!
# https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf

import numpy as np 

# Arrays are the core of numpy. These are containers, containing the same data
# type. 

# Examples of types:
type(1)
type(1.0) # a decimal number! (called float)

# Called float because the decimal point is moving around, or "floating".

type(sum)
type(list)
def f(x):
    return(x)
type(f)
type("i am a string")

# We will mostly (only) work with floats. Maybe integers.

x = np.array([0.01, 0.55, 0.9999, 5607, -1, -89.001, 5, 1])
x.dtype # float64 is "double precision" floats. SOmetimes "double".

# Arrays can be manipulated just like lists can.
x[0]
x[-1] 
x[0::2]
x[0:5:2]

# We can generate arrays in many ways in Numpy.
np.zeros(10)
np.ones(10)

# Recall the range function from base python:
list(range(0, 10 + 1)) # 0, 1, 2, 3 .... ,10
np.array(list(range(0, 10 + 1)))
## WRRONG WAY!
np.arange(0, 10 + 1)
np.arange(0, 20 + 1, 2)

# For plotting, you need to generate evenly spaced numbers between a and b. 
# For instance n of them.
# np.linspace(a, b, n)
np.linspace(1, 10, 19) # Notice the non-Pythonic upper limit. Function from Matlab.

# There are even more ways to generate arrays; look at the documentation.
# https://numpy.org/doc/stable/user/basics.creation.html

# Until now we have only covered one-dimensional arrays.
# But arrays have dimensions too!

x = np.array([[0.5, 0.2, 0.3],
              [100, 0.4, 0.5]])

# x[i, j] the element at the ith row and jth column.
x[1, 1] # 0.4
x[1, 1] = 0.42

x.shape # R * K: R. Kelly!

# We can reshape arrays!
x.reshape((3, 2))

# You want to be able to transpose arrays!
np.transpose(x)

# If you want to copy an array, use the x.copy() method!
z = x
z[0, 0] = -37
z
x # Oh no! It has changed!

# Need to use z = x.copy()!
z = x.copy()
z[0, 0] = -37
z
x # Stays the same!

## Vectorized operations!

# Say that you want to modify all the elements of two lists a and b.
a = [1, 2, 3]
b = [4, 5, 7]
a * b # = [4 = 1* 4, 10 = 2 * 5, 21 = 3 * 7]
# for two arrays a, b, i would like z = a * b to have the elements z[i ,j] =
# a [i,j] * b[i,j]

# Numpy does what we want!
a = np.array(a)
b = np.array(b)
a * b

# This way of operating is called vectorization. It's super important to use
# both for performance and good-looking code.
a + b
a - b
a / b
a ** b

# Let's look at comparisons.
a = np.array([1, 2, 3, 4, 5])
b = np.array([0, 3, 7, 9, 10])
a > b
np.maximum(a, b)
np.minimum(a, b)

# There are several important functions that work on just one array!
np.exp(a)
np.sqrt(a)

## But Numpy also has a couple of summarizing funcitons. 
np.sum(a) # Equivalent to a[0] + a[1] + ... + a[len(a) - 1]
np.prod(a) 
np.max(a)
np.min(a)
np.argmax(a) # returns the first index of a maximum
a = np.array([1, 2, 3, 4, 5, 1, 1, 1, 1, 5])
np.argmax(a)
np.argmin(a)

# We also have a couple of statistical functions!
np.mean(a)
np.median(a)
np.var(a) # The variance
np.sd(a) # Calculates the standard deviaiton!

# Numpy has some mathematical constants, namely
np.e 
np.pi

## Exercises:
## (i) Calculate the product of the first 100 numbers. That is, the product 1 *
## 2 * 3 * ... * 100
## (ii) Calculate the sum of the 100 first squares! 1** 2 + 2**2 + ... 100**2
## (iii) Find the variance of the first 100 squares!
## (iv) Approximate the minimum value of 5 * x ** 5 - 4 * x ** 3 + x on the 
## interval [-1,1]. (Hint: np.linspace and np.min).'
## (v) Find the x where 5 * x ** 5 - 4 * x ** 3 + x attains its minimum. [Hint:
## np.argmin] (This is still on the interval [-1, 1]).
## (vi) I want you to make a function f that calculates the sum of the n first
## reciprocal squares: f(n) = 1/1**2 + 1/2**2 + ... + 1/n**2. The plot the
## output of f when multiplied by 6 / pi ** 2. What happens? [Hint: (1/n)**2, not
## 1/n**2]. (Let n = 1 and 10 ** 5).