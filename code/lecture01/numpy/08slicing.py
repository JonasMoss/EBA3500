import numpy as np

a = np.arange(0, 10) ** 2
b = np.sin(np.linspace(-2 * np.pi, 2 * np.pi, 10))

c = np.vstack((a, b))
c
d = np.hstack((a, b))
d

b[b > 0]
c[c > 0]
(c[c > 0]).sum()

(d < 0) | (d % 2 == 0)
d[(d < 0) | (d % 2 == 0)]
