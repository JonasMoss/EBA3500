# Examples of built-in types
# https://docs.python.org/3/library/stdtypes.html

type(1)  # unlimited precision!
type(1.0)  # double precision floating point values; f64.
type(complex(1, 1))  # two f64s.

type("i am a string")
type(False)

type(sum)


def f(x):
    return x


type(f)
type(lambda x: x + 1)

type([1, 2, 3])
type({1, 2, 3})
type({1: "Coca Cola", 2: "Pepsi"})
type((1, 2))
