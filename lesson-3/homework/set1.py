def set_union(set1: set, set2:set):
  return set1 | set2 


set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
union_set = set_union(set_1, set_2)
print(f"Union: {union_set}")