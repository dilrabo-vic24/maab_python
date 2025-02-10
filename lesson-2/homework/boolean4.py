number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))
number3 = float(input("Enter number3: "))

check = (number1 != number2) and (number1 != number3) and (number2 != number3)

if(check):
    print("All of them are differen")
else:
    print("All of them are the same")