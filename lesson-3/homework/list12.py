def insert_element(lst, index, element):
  lst.insert(index, element)
  return lst

my_list = [1, 2, 3, 4, 5]
print(f"The new list with element inserted: {insert_element(my_list, 2, 10)}")