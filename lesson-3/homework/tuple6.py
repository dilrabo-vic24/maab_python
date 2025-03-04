def get_last_element_tuple(tup: tuple):

  if not tup:
    return "Tuple is empty"
  else:
    return tup[-1]

my_tuple = (7, 2, 7, 2, 7, 4, 2)

last_element = get_last_element_tuple(my_tuple)
print(f"The last element is: {last_element}")