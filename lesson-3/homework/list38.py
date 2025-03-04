def is_palindrome(lst):
  return lst == lst[::-1]

my_list = [1, 2, 3, 4, 3,  2, 1]
print(f"Is palindrome? {is_palindrome(my_list)}")