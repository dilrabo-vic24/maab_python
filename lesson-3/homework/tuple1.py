def count_occurrences_tuple(tup, element):
  count = 0
  for item in tup:
    if item == element:
      count += 1
  return count


my_tuple = (7, 2, 7, 2, 7, 4, 2)
element = 7
occurrences = count_occurrences_tuple(my_tuple, element)
print(f"Appearance time:  {occurrences}")