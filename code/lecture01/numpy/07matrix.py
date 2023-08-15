import numpy as np
np.set_printoptions(suppress=True)

# One-dimensional arrays: Or 'vectors'.
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

# Dot product
x.dot(y)
np.dot(x, y)
x @ y

# Matrix product
X = np.array([[1, 2, 3], [2, 1, 2], [3, 2, 1]])
Y = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 1]])
X @ Y

# Solve matrix equations
np.linalg.solve(X, x)

# Get the matrix inverse
np.linalg.inv(X)

# Y is not invertible / singular
np.linalg.inv(Y)

# Determinant
np.linalg.det(X)
np.linalg.det(Y)

# Transpose a matrix
Y
Y.T

# Element-wise (Hadamard) product
X * Y

X @ Y

# Extract the diagonal using diag.
np.diag(X)
np.diag(Y)

np.trace(X)
np.diag(X).sum()

# Eigenvectors and eigenvalues
np.linalg.eig(X)
np.linalg.eig(Y)[0].sum()
np.trace(Y)
