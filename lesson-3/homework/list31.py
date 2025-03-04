def repeat_elements(lst):
  new_lst = []
  for element in lst:
    new_lst.extend([element] * element)
  return new_lst

my_list = [1, 2, 3]
print(f"Repeated elements: {repeat_elements(my_list)}")