import numpy as np

A_circuit = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b_circuit = np.array([12, -5, 15])

currents = np.linalg.solve(A_circuit, b_circuit)

print("Task 4: Electrical Circuit Equations")
print(f"Coefficient matrix: \n{A_circuit}")
print(f"Constants: {b_circuit}")
print(f"Solution: I_1 = {currents[0]}, I_2 = {currents[1]}, I_3 = {currents[2]}")