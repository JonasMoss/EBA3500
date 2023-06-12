x = np.array([1, 2, 3])
y = np.array([5, 9, 4])

x - y
x * y
x / y
x**y

## Faster to write.

x = list(x)
y = list(y)

# unsupported operand
x - y
x * y
x / y
x**y

## Easier to understand
[x - y for x, y in zip(x, y)]
