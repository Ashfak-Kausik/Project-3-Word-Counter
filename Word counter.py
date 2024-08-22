def count_words(text):
    words = text.split()
    return len(words)

# Get input from the user
text = input("Enter a text: ")
word_count = count_words(text)
print(f"The text contains {word_count} words.")
