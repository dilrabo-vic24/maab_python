def concatenate_tuples(tuple1: tuple, tuple2: tuple) -> tuple:
  return tuple1 + tuple2

my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
print(f"New tuple: {concatenate_tuples(my_tuple1, my_tuple2)}")