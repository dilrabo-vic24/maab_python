def rotate_list(lst: list, k: int) -> list:
  n = len(lst)
  if n == 0:
    return []

  k = k % n

  new_lst = lst[-k:] + lst[:-k]
  return new_lst

my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

print(f"Rotated list: {rotate_list(my_list, 2)}")