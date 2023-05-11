### Here's some more info about default values! 
### Especially when they are difficult to understand.

### An easy example of default values.
def f(x, a = True): 
    if a:
        return (x + 1)
    if not a:
        return (x + 2)

### A more difficult example.

# f = lambda x: x is the identity function
def apply_and_square(x, f = lambda x: x):
    return [f(y) ** 2 for y in x]

# Its default argument is the identity function
x = [1, 2, 3, 4]
apply_and_square(x)

# Now let's use a non-default argument!
apply_and_square(x, f = lambda x: x ** (1/2))

# Let's take another one:
apply_and_square(x, f = lambda x: x ** 2)
[x ** 4 for x in x]

## Let's do somehting tricky:
apply_and_square(x, f = lambda x: x * sum(apply_and_square([x])))
apply_and_square(x, f = lambda x: x * apply_and_square([x])[0])
apply_and_square(x, f = lambda x: x * x ** 2)
apply_and_square(x, f = lambda x: x ** 3)
[(x ** 3) ** 2 for x in x]
[x ** 6 for x in x]