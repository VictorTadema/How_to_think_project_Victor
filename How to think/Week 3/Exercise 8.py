response1 = input("Length first side")
response2 = input("Length second side")
response3 = input("Length second side")

r1 = float(response1)
r2 = float(response2)
r3 = float(response3)

if r3 == (r1*r1+r2*r2)**0.5:
    print(True)
else:
    print(False)