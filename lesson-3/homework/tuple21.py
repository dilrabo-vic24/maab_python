def repeat_elements_tuple(tup):

  new_tup = ()
  for element in tup:
    new_tup += (element,) * element
  return new_tup

my_tuple = (1, 2, 3)
print(f"Repeated elements: {repeat_elements_tuple(my_tuple)}")