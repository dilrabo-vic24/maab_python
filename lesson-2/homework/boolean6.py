number = int(input("Enter number: "))

check = (not number % 15)
if(check):
    print("Divisible")
else:
    print("Not divisible")