def get_middle_element(lst):
  n = len(lst)

  if n == 0:
    return None

  if n % 2 == 0:
    mid1 = n // 2 - 1
    mid2 = n // 2
    return (lst[mid1]+ lst[mid2])//2
  else:
    mid = n // 2
    return lst[mid]

my_list = [5, 6, 4, 8, 9, 1]
print(f"Middle element: {get_middle_element(my_list)}")