import numpy as np

f64 = np.array([1.0, 2, 3, 4])
type(f64)

f64.dtype 
np.finfo(f64.dtype) #floating point info.

# Floating points are imprecise!

print(f"{(0.1 + 0.2):.52f}")

# Exercise: Use the f string to print 0.5 * 2 to high precision and 0.5 * 0.4.

print(f"{(0.5 * 2):.64f}")
print(f"{(0.5 * 0.4):.54f}")