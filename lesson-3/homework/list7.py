def get_last_element(lst:list):
  if not lst:
    return None
  else:
    return lst[-1]
lst = [1, 2, 3, 4, 5]
last_element = get_last_element(lst)
print(f"The first is: {last_element}")
