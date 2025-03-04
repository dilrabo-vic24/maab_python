def reverse_tuple(tup: tuple) ->tuple:
  return tup[::-1]

my_tuple = (1, 2, 3, 4, 5,)
print(f"Reversed tuple: {reverse_tuple(my_tuple)}")