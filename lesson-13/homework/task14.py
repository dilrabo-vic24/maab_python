import  numpy as np


A = np.random.random((3, 3))
b = np.random.random(3)
x = np.linalg.solve(A, b)
print("Solution to the linear system Ax = b:")
print("Matrix A:")
print(A)
print("Vector b:")
print(b)
print("Solution x:")
print(x)
print("Verification A.x == b:", np.allclose(np.dot(A, x), b))