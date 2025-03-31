import  numpy as np


matrix_5x5 = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5, axis=1)
column_sums = np.sum(matrix_5x5, axis=0)
print("Row-wise and column-wise sums of a 5x5 matrix:")
print("Matrix:")
print(matrix_5x5)
print("Row sums:")
print(row_sums)
print("Column sums:")
print(column_sums)