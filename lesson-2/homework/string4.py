text = input("Enter text: ")

reversed_text = text[::-1]

if(text == reversed_text):
    print("Palindrom")
else:
    print("Not palindrom")