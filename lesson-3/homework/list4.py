def min_element(lst: list):
  if not lst:
    return None

  if not all(isinstance(item, (int, float)) for item in lst):
      raise TypeError("List must contain only numbers (integers or floats).")

  min_value = lst[0]
  for num in lst:
    if num < min_value:
      min_value = num
  return min_value


lst = [9, 5, 2, 8, 3]
print(f"Min(min_element): {min_element(lst)}")
print(f"Min(python function): {min(lst)}")