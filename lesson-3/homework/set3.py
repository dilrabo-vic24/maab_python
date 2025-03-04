def set_difference(set1: set, set2:set) -> set:
  return set1 - set2

set_a = {1, 2, 3}
set_b = {3, 4, 5}
difference_set = set_difference(set_a, set_b)
print(f"Difference of set1: {difference_set}")