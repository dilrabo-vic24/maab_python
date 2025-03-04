def find_second_largest_tuple(tup):
  
  unique_elements = sorted(list(set(tup)))
  if len(unique_elements) < 2:
    return None
  return unique_elements[-2]

my_tuple = (1, 5, 2, 8, 3)
print(f"Second largest element: {find_second_largest_tuple(my_tuple)}")