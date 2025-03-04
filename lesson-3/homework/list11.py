def remove_duplicates(lst):
  new_lst = []
  for item in lst:
    if item not in new_lst:
      new_lst.append(item)
  return new_lst

my_list = [1, 2, 2, 3, 4, 4, 5]
print(f"New list: {remove_duplicates(my_list)}")