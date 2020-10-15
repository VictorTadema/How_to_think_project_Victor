def reverse(text):
    reverso = ""
    for i in range(len(text) - 1, -1, -1):
        reverso += text[i]
    return reverso


print(reverse("bier"))


def mirror(text):
    return text + reverse(text)

print(mirror("bavje"))