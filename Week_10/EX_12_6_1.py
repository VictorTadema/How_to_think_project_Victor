# Write a function named readposint that uses the input dialog to prompt the user for a positive integer and
# then checks the input to confirm that it meets the requirements. It should be able to handle inputs that cannot be
# converted to int, as well as negative ints, and edge cases (e.g. when the user closes the dialog, or does not
# enter anything at all.)

def readposint():
    try:
        number = int(input("Please enter positive number: "))
    except ValueError:
        print("A number! you stupid")
    if number < 0:
        raise ValueError("{0} a POSITIVE number lil bitch".format(number))


readposint()
