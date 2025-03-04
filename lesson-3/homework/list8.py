def get_first_three(lst:list) -> None:
  if(len(lst) < 3):
    print("Length of list is less than 3")
  else:
    print(f"{lst[:3]}")

lst = [1, 2, 3, 4, 5]
get_first_three(lst)