def create_subtuples(tup, sub_tuple_size):
  if not tup or sub_tuple_size <= 0:
    return ()

  new_tup = ()
  for i in range(0, len(tup), sub_tuple_size):
    new_tup += (tup[i:i + sub_tuple_size],)
  return new_tup

my_tuple = (7, 2, 1, 4, 6, 19, 7, 11, 9)
print(f"Subtuples: {create_subtuples(my_tuple, 3)}")