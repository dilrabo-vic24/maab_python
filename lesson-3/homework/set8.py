def remove_element(set1, element):

  set1.discard(element)
  return set1


my_set = {1, 2, 3}
element = 2

my_set = remove_element(my_set, element)

print(f"Set after removal: {my_set}")