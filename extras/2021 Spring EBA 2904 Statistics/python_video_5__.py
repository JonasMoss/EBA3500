# An introduciton to numpy!
# https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf

import numpy as np 

# Arrays are the core of numpy. These are containers, containing data of the 
# same type.

# Examples of types:
type(1)
type("i'm a string")
type(sum)

def f(x): 
    return(x)

type(f)
type(0.01) # A floating point decimal number.

# "floats" has nothing to do with floating on water! It is called a float 
# because the decimal marker to move, or to "float".

# We will only work with arrays of the type float! 
x = np.array([0.01, 0.55, 0.9999, 5607, -1, -89.001, 5, 1])
x.dtype # 64-bit floating number; same as float (sometimes called "double")
# In older languages, such as C++, float is 32 bit and "double" is 64 bit.

# Arrays can be manipulated just like lists:
x[0]
x[-1]
x[0::2]
x[0:5:2]

# Numpy has many functions generating arrays!
np.zeros(10)
np.ones(10)

# Recall the range function! 
list(range(0, 10 + 1))
np.array(range(0, 10 + 1))
np.arange(0, 10 + 1)
np.arange(0, 15, 2)

# For plotting you need to generate evenly spaced numbers between a and b.
# Say you want n of these of these numbers.
# Then you would use np.linspace(a, b, n).
np.linspace(1, 10, 199)

# Other ways to generate array exist, see the documentation:
# https://numpy.org/doc/stable/user/basics.creation.html

# Have only covered one-dimensional arrays til now.

# But arrays have dimensions too!

x = np.array([[0.5, 0.2, 0.3],
         [100, 0.4, 0.5]])

x.shape # 2 rows, 3 columns: Think R Kelly, row kolumn.

# The dimensions of an array are called "axes" in numpy!
y = np.array([[[0.5, 0.2], [1, 0.3]], 
              [[100, 0.4], [0.5, 7]]])

# You can reshape it!
x.reshape((3, 2))

# Transpose! 
np.transpose(x)

# If you want to copy an array, you usually don't want to do this:
z = x
z
z[0, 0] = 100 # this is the top-left most element of the array.
# z[i, j] is the element with row-index i and column-index j.
z[1, 1] = 99 
x # I didn't want that to change!

# Make a copy of x instead!
x = np.array([[0.5, 0.2, 0.3],
         [100, 0.4, 0.5]])
z = x.copy()
z[1, 1] = 99
z
x # Is still the same.

## Vectorized operations!

# Say you want to modify all the elements of two lists a and b.
a = [1, 2, 3]
b = [5, 6, 7]
a * b # [5 = 1 * 5, 12 = 2 * 6, 21 = 3 * 7]

# Can do this numpy! The is called vectorized operations. It's super important
# to use these operations: Both for succinct code and for understable code!
a = np.array(a)
b = np.array(b)
a * b

# This works with other operations too:
a / b
a + b
a - b
a ** b

# You might be interested in maximum and minimum.
a = np.array([1, 2, 3])
b = np.array([0, 3, 7])
np.maximum(a, b) # [1, 3, 7]
np.minimum(a, b)
a > b

# There are many functions that work on a single array: 
np.exp(a)
np.sin(a)
np.sqrt(a)

# Functions that "summarize" an array, f: A -> floats
np.sum(a)
np.prod(a)
np.max(a)
np.min(a)
np.argmax(a)
np.argmin(a)

# We have several statistical functions:
np.mean(a)
np.median(a)
np.var(a)
np.sd(a)

# numpy has important constants built in:
np.e 
np.pi

## Exercises:
## (i) Calculate the product of the first 100 numbers. That is, the product of 
## all the numbers 1, 2, 3, 4, ... , 100
## (ii) Calculate the sum of the first 100 squares. 1 ** 2 + 2 ** 2 + 3 ** 3 + 
## + ... + 100 ** 2
## (iii) Calculate the variance of the first 100 squares.
## (iv) Approximate the minimum value of 5 * x ** 5 - 4 * x ** 3 + x, on the 
## interval [-1, 1]. (Hint: You have to use the np.min function.)
## (v) What is the value of the x where  5 * x ** 5 - 4 * x ** 3 + x attains its
## minimum on [-1, 1]. (Hint: Use the argmax function.)
## (vi) Make a function that calculates the sum of the n first reciprocal squares.
## Calcualte 1 / 1 ** 2 + 1 / 2 ** 2 + ... + 1 / n ** 2. Plot the output of this
## function when multiplied by 6 / pi ** 2 for n = 1, ... 10 ** 5. (You want to
## plot f(n) * 6 / pi ** 2, where f is the function you made.) [Hint: Use 
## (1 / n) ** 2 NOT 1 / n ** 2.]