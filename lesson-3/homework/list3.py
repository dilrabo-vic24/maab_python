def max_element(lst: list):
  if not lst:
    return None

  if not all(isinstance(item, (int, float)) for item in lst):
      raise TypeError("List must contain only numbers (integers or floats).")

  max_value = lst[0]
  for num in lst:
    if num > max_value:
      max_value = num
  return max_value


lst = [1, 5, 2, 8, 3]
print(f"Max(max_element): {max_element(lst)}")
print(f"Max(python function): {max(lst)}")