import numpy as np

A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)

print("Task 3: System of Equations")
print(f"A = \n{A}")
print(f"b = {b}")
print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")