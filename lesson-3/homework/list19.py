def replace_element(lst, old_element, new_element):
  new_lst = lst[:]
  try:
    index = new_lst.index(old_element)
    new_lst[index] = new_element
  except ValueError:
    pass
  return new_lst

my_list = [1, 2, 3, 2, 4, 5]
print(f"Old list: {my_list}")
print(f"The new list is: {replace_element(my_list, 2, 10)}")