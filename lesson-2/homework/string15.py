sentence = input("Enter sentence: ")
words = sentence.split()
acronym = ""

for word in words:
    acronym += word[0].upper()

print(f"Acrony: {acronym}")