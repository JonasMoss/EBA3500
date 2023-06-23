import numpy as np

x = np.array([1, 2, 3])
y = np.array([5, 9, 4])

x - y
x * y
x / y
x**y

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

## Easier to read
[xl - yl for xl, yl in zip(xl, yl)]
x - y

## Faster!


def f_python(x, y):
    return sum([x * y for x, y in zip(x, y)])


def f_numpy(x, y):
    return (x * y).sum()


from tinybench import benchmark, benchmark_env

x = np.arange(0, 10000, 2)
y = np.arange(1, 10001, 2)
xl = list(x)
yl = list(y)

bench = benchmark(
    ["f_python(xl, yl)", "f_numpy(x, y)"], ntimes=1000, warmup=10, g=globals()
)
bench.means
bench.means["f_python"] / bench.means["f_numpy"]
