text = input("Enter text: ")
has_digit = False

for i in text:
    if i.isdigit():
        has_digit = True
        break

if has_digit:
    print("Text has digit")
else:
    print("Text doesn't have digit")