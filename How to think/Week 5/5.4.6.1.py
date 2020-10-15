letter_counts = {}
for letter in "ThiS is String with Upper and lower case Letters":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_counts.items().lower()
letter_items = list(letter_counts.items())

letter_items.sort()
print(letter_items)

