import random

num_elements = 5
min_value = 1
max_value = 10

if num_elements > (max_value - min_value + 1):
    print("Warning: Number of elements exceeds the range, set may contain duplicates.")

random_set = set()

while len(random_set) < num_elements:
    random_set.add(random.randint(min_value, max_value))

print(f"Random set: {random_set}")