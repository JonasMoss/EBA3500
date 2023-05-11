# An introduction to Numpy!
# https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf

import numpy as np

# Arrays are the core of numpy. These are containers containing data of the same
# type. 

# Examples of types:
type(1)
type("i'm a string")
type(sum)
type(0.01) # A floating point decimal number.

# Floats have nothing to do with floating on water! It's technical; it means
# the placement of the decimal is allowed to move around (that is, it floats.)

# We will only use arrays with floats. You can make arrays from lists and other
# iterators using np.array 
x = np.array([0.01, 0.55, 0.9999, 5607, -1, -89.001, 5, 1])
x.dtype 
# "float64" is often called "double". This is double precision floating points,
# just called "float" in python.

# Arrays can be manipuled similarily to lists:
x[0]
x[-1]
x[0::2]
x[0:6:2]

# Numpy has many functions that generate (deterministic) arrays:
np.zeros(10)
np.ones(10)

# The range(start, stop) function from Python has its numpy analogue. We use it
# quite often!
np.arange(0, 15)
np.arange(0, 15, 2)

# For plotting you'd like n evenly spaced points between a to b, or
# np.linspace(a, b, n)
np.linspace(1, 10, 19)

# There are other ways to generate matrices too. The documentation is here:
#  https://numpy.org/doc/stable/user/basics.creation.html

# But numpy arrays have dimensions too!
x = np.array([[0.5, 0.2, 0.3], 
              [100, 0.4, 0.5]])
x.shape # 2 rows, 3 columns. Think "R. Kelly": row kolumn. 
# These dimensions are called axes in numpy. We can have more dimensions too:
y = np.array([[[0.5, 0.2], [1, 0.3]], 
              [[100, 0.4], [0.5, 7]]])

y[0, ]

# You can reshape your arrays using the reshape method:
x.reshape((3, 2))

# And you can switch the column and rows using the transpose function; this is
# an easier way to do what we did above.
np.transpose(x)

# If you want to copy an array, you usually don't want to do this:
z = x
z
z[0, 0] = 0 
z
x # I didn't want that to change!

# Use x.copy() instead.
x = np.array([[0.5, 0.2, 0.3], 
              [100, 0.4, 0.5]])
z = x.copy()
z
z[0, 0] = 0 
z
x

## Vectorized operations!

# Say you want to multiply all the elements of two lists a and b
a = [1, 2, 3]
b = [5, 6, 7]
a * b # Oh no!

# But it works with numpy! This is called vectorized operations. It's super 
# important both for performance and writing succinct and understandable code.
a = np.array(a)
b = np.array(b)
a * b # Yes! It worked!

# Also works for the other standard mathematical operations:
a + b
a - b
a / a
a ** b

# And it works with numpy functions, such as the exponential function!
np.exp(a)
np.sqrt(a)

# Moreover, we can even compare array element-wise
a = np.array([1, 2, 3])
b = np.array([0, 3, 7])
a > b

# You can do this with maximum and minimum too:
np.maximum(a, b) 
np.minimum(a, b) 

# Note: If you've had linear algebra, a * b is not matrix multiplication, even
# when the array is two-dimensional.

# Numpy can do the obvious stuff with arrays. The following functions use every
# element of the array, regardless of dimension.
a = np.array([[1, 2, 3], 
              [4, 5, 6]])
np.sum(a) # This should be (6 + 1) * 6 / 2 of course ;)
np.prod(a)
np.max(a)
np.min(a)
np.argmax(a)
np.argmin(a)

# These can also be called as methods:
a.min()
a.max()

# We will use the functions, mostly because we will take functions as arguments
# to other functions.

# And we can use statistical functions:
np.mean(a)
np.var(a) # variance.
np.median(a)
np.sd(a) # standard deviation.

# numpy contains the most important mathematical constants
np.pi
np.e

## Exercises:
## i) Calculate the product of the first 100 numbers. That is, the product of 
##    all the numbers 1, 2, 3, 4, ..., 100.
## ii) Calculate the sum of the first 100 squares. That is, 1 + 2**2 + 3**2 + 
##    ... + 100**2
## iii) Calculate the variance of the first 100 squares.
## iv) Approximate the minimum value of 5 * x**5 - 4 * x**3 + x on the interval 
##    [-1, 1]. 
## v) At what value of x did 5 * x**5 - 4 * x**3 + x attain its minimum on the
##    interval [-1,1]?
## vi) Make a function f that calculates the sum of the n first reciprocal 
##   squares, i.e., 1 + 1/2 ** 2 + 1 / 3 ** 2 + ... 1 / n ** 2. Plot the output
##   of this function when multiplied by 6 / pi ** 2, or f(n) * 6 / pi ** 2
##   What happens as you increase n? Hint: Use (1 / n) ** 2, not 1 / n ** 2.
##   What does this mean?
