def password_checker():
    password = input("Parolingizni kiriting: ")

    if len(password) < 8:
        print("parol qisqa.")
    elif not any(char.isupper() for char in password):
        print("parolni to'g'ri kiritdingiz.")
    else:
        print("parol uzun.")

password_checker()