import numpy as np

def calculate_power(number, power):
    return number ** power

vectorized_power = np.vectorize(calculate_power)

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])
results = vectorized_power(numbers, powers)

print("Task 2: Power Calculation")
print(f"Numbers: {numbers}")
print(f"Powers: {powers}")
print(f"Results: {results}")