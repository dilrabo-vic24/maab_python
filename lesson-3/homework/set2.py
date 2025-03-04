def set_intersection(set1:set, set2:set) -> set:

  return set1 & set2

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
intersection_set = set_intersection(set_1, set_2)
print(f"Intersection set: {intersection_set}")