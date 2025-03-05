def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

number = int(input("Enter number = "))
print(is_prime(number))