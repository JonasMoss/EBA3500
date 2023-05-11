# Let's say you have a list of integers x. You want to square all of them and
# put them into a new list. How would you do it?
x = [1, 6, 9, 1, 6, 3, 0]

### (1) Here's one way to 
y = [0] * len(x)
for i in range(0, len(x)):
    y[i] = x[i] ** 2
print(y)

### (2) Here's another, more fancy, way of doing it:
y = [0] * len(x)
for i, elem in enumerate(x):
    y[i] = elem ** 2
print(y)

# How does this work?
for z in enumerate(x):
    print(z)

# Unpack z by i, elem = z, so that
for i, elem in enumerate(x):
    print(str(i) + " and " + str(elem))

# These ways work, but are wrong. The right way to do it is using list comprehensions.
y = [elem ** 2 for elem in x]
print(y)

# This way of writing y is the same as 1, just easier to write, read, and
# less bug-prone!

## Let's say you have a list of integers, but you want to square only the positive
## integers and ditch the rest!

x = [-1, 6, -9, 1, 6, -3, 0]

# Here's how to do it without list comprehensions:
y = []
for elem in x:
    if elem > 0:
        y.append(elem ** 2)
print(y)

# Here's how to do it with list comprehensions:
y = [elem ** 2 for elem in x if elem > 0]
print(y)

# You can also use dictionary comprehensions using curly braces:
# Make a look-up table for the ten first squared positive integers.
squares = {k : k ** 2 for k in range(1, 11)}

# This pattern is useful if {k : f(k) for k in x} when f takes a bit of time
# to compute.