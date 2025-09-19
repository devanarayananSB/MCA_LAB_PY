text = input("Enter a line: ")
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print(word_count)
