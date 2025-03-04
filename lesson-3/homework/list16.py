def count_odd_numbers(lst):
  count = 0
  for num in lst:
    if num % 2:
      count += 1
  return count

my_list = [1, 2, 3, 4, 5, 6]
print(f"The number of odd numbers: {count_odd_numbers(my_list)}")