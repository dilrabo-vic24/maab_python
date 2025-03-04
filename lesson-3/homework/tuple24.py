def is_palindrome_tuple(tup):

  return tup == tup[::-1]

my_tuple = (1, 2, 3, 4, 3, 5,  2, 1)
print(f"Is palindrome? {is_palindrome_tuple(my_tuple)}")