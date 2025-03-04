def index_of_element(lst, element):
  try:
    return lst.index(element)
  except ValueError:
    return -1

my_list = [1, 2, 3, 4, 5, 2]
print(f"Index: {index_of_element(my_list, 2)}")