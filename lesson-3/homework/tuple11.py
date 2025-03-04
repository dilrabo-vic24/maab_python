def find_all_indices(tup: tuple, element: int) -> list:
  indices = []
  for i, value in enumerate(tup):
    if value == element:
      indices.append(i)
  return indices

my_tuple = (7, 2, 3, 7, 4, 2, 5, 7, 10)
element = 7
print(f"Indices: {find_all_indices(my_tuple, element)}")