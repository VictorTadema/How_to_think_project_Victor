numbers = [-3, 1, 2, 3, 4, 5, 6, 7, 9]   #Just an example to make it less abstract and able to check answers
# Ex. 23
count = 0
for number in numbers:
    if number % 2 == 1:
        count += 1
print (count)

# Ex. 24
tot1 = 0
for number in numbers:
    if number % 2 == 0:
        tot1 += number
print (tot1)

# Ex. 25
tot2 = 0
for number in numbers:
    if number < 0:
        tot2 += number
print (tot2)

# Ex. 26
ExSen = "Type in your words fagot"
Count1 = 0
for word in map(len, ExSen.split()):
    if word == 5:
        Count1 += 1
print(Count1)

# Ex. 27 ?????????????




