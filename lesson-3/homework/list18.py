def find_sublist(lst, sublist):
  n = len(lst)
  m = len(sublist)

  if m == 0:
    return True

  for i in range(n - m + 1):
    if lst[i:i+m] == sublist:
      return True

  return False

my_list = [1, 2, 3, 4, 5, 6]
my_sublist = [2, 3, 4]

print(find_sublist(my_list, my_sublist))