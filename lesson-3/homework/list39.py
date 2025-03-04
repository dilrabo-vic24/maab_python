def create_sublists(lst, sublist_size):
  
  if not lst or sublist_size <= 0:
    return []

  new_lst = []
  for i in range(0, len(lst), sublist_size):
    new_lst.append(lst[i:i + sublist_size])

  return new_lst

my_list = [7, 2, 1, 4, 6, 19, 7, 11, 9]
print(f"Sublists: {create_sublists(my_list, 3)}")