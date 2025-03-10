import os
from collections import Counter

def get_text():

    if not os.path.exists("sample_text.txt"):
        print("sample_text.txt Not found. Enter new text: ")
        with open("sample_text.txt", "w") as file:
            text = input("Text: ")
            file.write(text)

def read_and_count():
    with open("sample_text.txt", "r") as file:
        text = file.read().lower()

    # text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    total_words = len(words)

    word_count = Counter(words)
    top_words = word_count.most_common(5)

    return total_words, top_words

def save_report(total_words, top_words):
    
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")


get_text()
total_words, top_words = read_and_count()

print(f"Total words: {total_words}")
print("Top 5 most common words:")

for word, count in top_words:
    print(f"{word} - {count} times")

save_report(total_words, top_words)
