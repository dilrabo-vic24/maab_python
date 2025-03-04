def find_all_indices(lst, element):
  indices = []
  for i, value in enumerate(lst):
    if value == element:
      indices.append(i)
  return indices

my_list = [7, 2, 3, 7, 4, 2, 5, 7, 10]
element = 7
print(f"Indices: {find_all_indices(my_list, element)}")