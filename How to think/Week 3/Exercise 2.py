# Exercise 2
response1 = input("When do you start off?")
response2 = input("How long is your stay?")
Start = float(response1)
Length = float(response2)
Days = Length % 7
Day = Start + Days
if Day == 1:
    print("Sunday")
if Day == 2:
    print("Monday")
if Day == 3:
    print("Tuesday")
if Day == 4:
    print("Wednesday")
if Day == 5:
    print("Thursday")
if Day == 6:
    print("Friday")
if Day == 7:
    print("Saturday")
