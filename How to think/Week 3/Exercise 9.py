
response1 = input("Length first side")
response2 = input("Length second side")
response3 = input("Length second side")

x1 = float(response1)
x2 = float(response2)
x3 = float(response3)

if x1 > x2 and x3:
    r3 = x1
    r2 = x2
    r1 = x3
if x2 > x1 and x3:
    r3 = x1
    r2 = x2
    r1 = x3
if x3 > x2 and x1:
    r3 = x1
    r1 = x2
    r2 = x3

if r3 == (r1*r1+r2*r2)**0.5:
    print(True)
else:
    print(False)