import numpy as np

matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product = np.dot(matrix_5x3, matrix_3x2)
print("Matrix product of 5x3 and 3x2 matrices:")
print(matrix_product)