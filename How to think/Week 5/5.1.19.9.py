def remove_letter(letter, text):
    clear = ""
    for _ in text:
        if _ != letter:
            clear += _
    return clear

x = remove_letter("a", "appelflap")
print (x)