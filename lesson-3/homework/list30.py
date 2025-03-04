def is_sorted(lst):
  if not lst:
    return True

  for i in range(len(lst) - 1):
    if lst[i] > lst[i+1]:
      return False

  return True

my_list = [5, 2, 3, 4, 1]
print(is_sorted(my_list))

my_list2 = [1, 2, 3, 4, 5]
print(is_sorted(my_list2))