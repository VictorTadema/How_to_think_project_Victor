def sum_to(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a

answer = int(input("What value to sum?"))
print(sum_to(answer))

