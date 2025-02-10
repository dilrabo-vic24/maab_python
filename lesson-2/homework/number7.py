number_str = input("Enter a number: ")

if number_str.isdigit():

    if int(number_str) % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Please enter an integer.")