import  numpy as np


random_3x3 = np.random.random((3, 3))
column_vector = np.random.random((3, 1))
matrix_vector_product = np.dot(random_3x3, column_vector)
print("Matrix-vector product:")
print("Matrix:")
print(random_3x3)
print("Column vector:")
print(column_vector)
print("Product:")
print(matrix_vector_product)