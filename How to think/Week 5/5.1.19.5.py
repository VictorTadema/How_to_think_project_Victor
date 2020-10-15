text = "Hey jij daar de zwemmende walvis, de walvis met watervrees"

words_text = text.split()
amount = len(words_text)

total_e = 0
for word in words_text:
    if "e" in word:
        total_e += 1

percentage = total_e / amount *100
print("Your text contains {} words, of which {} ({:.1f}%) contain an 'e'.".format(amount, total_e, percentage, "e"))


