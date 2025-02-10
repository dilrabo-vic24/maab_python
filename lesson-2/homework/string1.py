import datetime

name = input("Enter your name: ")
year_str = input("Enter your year of birth: ")

if year_str.isdigit():
    year = int(year_str)
    current_year = datetime.datetime.now().year
    age = current_year - year
    if age > 0:
        print(f"Your age is {age}")
    else:
        print("Enter your correct birth year")

else:
    print("Year is not in valid")