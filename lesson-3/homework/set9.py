def clear_set(set1):
  set1.clear()
  return set1

my_set = {1, 2, 3}
my_set = clear_set(my_set)

print(f"Cleared set: {my_set}")