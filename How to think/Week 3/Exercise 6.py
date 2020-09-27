numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for number in numbers:
    if number >= 75:
         print ("Grade = First")
    if 70 >= number > 75:
         print("Grade = Second")
    if 60 >= number > 70:
         print("Grade = Third")
    if 50 >= number > 60:
         print("Grade = F1")
    if 45 >= number > 50:
         print("Grade = F2")
    if number < 45:
         print("Grade = F3")