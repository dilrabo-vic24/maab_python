def remove_element_by_index(lst, index):
  try:
    lst.pop(index)
  except IndexError:
    return lst[:]
  return lst


my_list = [1, 2, 3, 4, 5]
print(f"My list: {my_list}")
print(f"New list: {remove_element_by_index(my_list, 2)}")