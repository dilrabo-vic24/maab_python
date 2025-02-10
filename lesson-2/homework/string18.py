text = input("Enter text: ")

text_list = text.split()

first_word = text_list[0]
last_word = text_list[-1]
if(first_word == last_word):
    print("First and last words are the same")
else:
    print("First and last words are different")