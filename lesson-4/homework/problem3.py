txt = "hello"

result = ""
for i in range(len(txt)):
    result += txt[i]
    # Check if character is a vowel or every third character
    if txt[i] in ("a",'i','o','u','e') or (i + 1) % 3 == 0:
        # Ensure it's not the last character
        if i != len(txt)-1:
            result += "_"

print(result)