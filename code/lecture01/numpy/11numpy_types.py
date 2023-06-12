import numpy as np

x64 = np.array([1, 2, 3, 4])
type(x)

x64.dtype
np.iinfo(x64.dtype)  # integer info.

# Overflow
np.array(9223372036854775807) + 1

# Never a problem with Python:
9223372036854775807 + 1

# There are other integer values
x32 = np.array([1, 2, 3, 4], np.int32)
np.iinfo(x32.dtype)

# Available types for signed integers can be found using IntelliSense.


# There are also unsigned integer, e.g. np.uint32.
