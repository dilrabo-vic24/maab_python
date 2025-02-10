text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"Vowels {vowel_count}\nConsonants {consonant_count}")