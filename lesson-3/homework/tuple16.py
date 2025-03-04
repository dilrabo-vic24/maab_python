def is_tuple_sorted(tup):
  if not tup:
    return "Tuple is empty"

  for i in range(len(tup) - 1):
    if tup[i] > tup[i+1]:
      return False

  return True

my_tuple = (1, 2, 3, 4, 5, 6)

print(f"Is sorted? {is_tuple_sorted(my_tuple)}")