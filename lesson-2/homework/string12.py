def myfunc():
    text = input("Enter words: ")
    words = text.split()

    separator = input("Enter separator ('-' or ','): ")
    if separator not in ['-', ',']:
        print("Invalid separator")
        return

    result = separator.join(words)
    print(f"Joined string: {result}")

myfunc()