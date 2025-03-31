import numpy as np 

random_10x10 = np.random.random((10, 10))

min_value = random_10x10.min()
max_value = random_10x10.max()

print("10x10 array min and max values:")
print(f"Min value: {min_value}")
print(f"Max value: {max_value}")