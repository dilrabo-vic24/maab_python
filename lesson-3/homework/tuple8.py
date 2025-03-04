def get_first_three_tuple(tup: tuple) -> tuple:
  return tup[:3]

my_tuple = (7, 2, 7, 2, 7, 4, 2)

new_tuple = get_first_three_tuple(my_tuple)
print(f"New tuple: {new_tuple}")