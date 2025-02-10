num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
  print("Error: Division by zero is not allowed.")
else:
  integer_division = num1 // num2
  theremainder = num1 % num2
  print(f"Integer quotient: {integer_division}")
  print(f"Remainder: {theremainder}")