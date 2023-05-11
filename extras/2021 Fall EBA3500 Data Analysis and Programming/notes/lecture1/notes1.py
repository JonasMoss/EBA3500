import numpy as np

x = np.array([3, 1, 2])
y = np.array([1, 8, 3])

A = np.array([[2,-5,3],
[0,7,-2],
[-1,4,1]])

B = np.array([[2,1,1],
[3,2,1],
[2,1,2]])

np.transpose(A @ B)
np.transpose(B) @ np.transpose(A)

np.transpose(np.linalg.inv(A))
np.linalg.inv(np.transpose(A))


A = np.array([[1,0,1],

[0,1,0],
[1,0,1]])

B = np.array([[1,2,2],
[2,1,3],
[3,2,1]])

z = np.array([1, 2, 3])

x = np.array([2,2,1])
y = np.array([1,3,3])
