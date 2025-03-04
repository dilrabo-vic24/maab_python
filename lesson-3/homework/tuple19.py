def remove_element_by_value_tuple(tup: tuple, element: float) -> tuple:
  
    index = tup.index(element)
    new_tup = tup[:index] + tup[index+1:]
    return new_tup


my_tuple = (1, 2, 3, 2, 4, 5)
print(f"Modified tuple: {remove_element_by_value_tuple(my_tuple, 2)}")