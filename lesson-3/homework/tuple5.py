def get_first_element_tuple(tup: tuple):

  if not tup:
    return "Tuple is empty"
  else:
    return tup[0]

my_tuple = (7, 2, 7, 2, 7, 4, 2)

first_element = get_first_element_tuple(my_tuple)
print(f"The first element is: {first_element}")