def is_tuple_empty(tup: tuple) -> bool:
  return not tup

my_tuple = (1, 2, 3)
print(is_tuple_empty(my_tuple))

empty_tuple = ()
print(is_tuple_empty(empty_tuple))