def check_element(lst:list, element: any) -> bool:
  return element in lst

my_list = [1, 2, 3, 4, 5]
element1 = 3
element2 = 6

print(f"{element1} {check_element(my_list, element1)}")
print(f"{element2} {check_element(my_list, element2)}")