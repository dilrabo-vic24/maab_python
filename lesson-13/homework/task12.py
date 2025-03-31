import  numpy as np


matrix_A_3x4 = np.random.random((3, 4))
matrix_B_4x3 = np.random.random((4, 3))
product_A_B = np.dot(matrix_A_3x4, matrix_B_4x3)
print("Matrix product of A (3x4) and B (4x3):")
print(product_A_B)