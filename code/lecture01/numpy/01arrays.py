import numpy as np

# Sum the elements of two lists elementwise.
x = [1, 2, 3]
y = [5, 9, 4]
z = zip(x, y)
list(z)

z = [x + y for x, y in zip(x, y)]
z

x = np.array([1, 2, 3])
y = np.array([5, 9, 4])
z = x + y
z

## Numpy arrays are typed!
z.dtype


## More vectorize operations
x - y
x * y
x / y
x**y

## 3 Benefits

## Faster to write.

xl = list(x)
yl = list(y)
xl
yl

# unsupported operand!
xl - yl
xl * yl
xl / yl
xl**yl

# Sometimes operands are supported even for non-numeric values.
"a" + "b"

# 1. Easier to read.
# 2. Faster to write.
# 3. Faster to run!


## Easier to read
[xl - yl for xl, yl in zip(xl, yl)]
x - y


## Faster
def dot_python(x, y):
    """Calculate dot product in vanilla Python."""
    return sum([x * y for x, y in zip(x, y)])


def dot_numpy(x, y):
    """Calculate dot product with Numpy."""
    return (x * y).sum()


## Numpy is faster.
from tinybench import benchmark, benchmark_env

x = np.arange(0, 10000, 2)
y = np.arange(1, 10001, 2)
xl = list(x)
yl = list(y)

bench = benchmark(
    ["dot_python(xl, yl)", "dot_numpy(x, y)"], ntimes=10000, warmup=10, g=globals()
)

bench.means
bench.means["dot_python"] / bench.means["dot_numpy"]
