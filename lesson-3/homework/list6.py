def get_first_element(lst):
  if not lst:
    return None
  else:
    return lst[0]

my_list = [1, 2, 3, 4, 5]
first_element = get_first_element(my_list)
print(f"The first element of {my_list} is: {first_element}")