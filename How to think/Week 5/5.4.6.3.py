word_counts = {}
for word in "Hey my name is diederik":
    word_counts[word] = word_counts.get(word, 0) + 1


word_items = list(word_counts.items())
word_items.sort()
print(word_items)
