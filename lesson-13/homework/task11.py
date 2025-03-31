import  numpy as np


matrix_for_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_for_det)
print("Determinant of a 3x3 matrix:")
print(f"Matrix:")
print(matrix_for_det)
print(f"Determinant: {determinant}")