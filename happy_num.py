def sum_of_sq(n):
    s = 0
    while (n > 0):
        s += (n % 10) ** 2
        n //= 10

    if len(str(s)) == 1:
        return s
    else:
        return sum_of_sq(s)

n = int(input("Enter a number:" ))
f = sum_of_sq(n)
if f == 1:
    print(n, " is a Happy number")
else:
    print(n, " is not a Happy number")
