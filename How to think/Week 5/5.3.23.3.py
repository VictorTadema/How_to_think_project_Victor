a = [1, 2, 3]
b = a[:]
b[0] = 5

print (a)
print (b)

# as one could conclude, a and b were and are not aliased. But before the 3. command, both rejected to the same value,
# after the this 3. command this was not the case. They refer to distinct values.