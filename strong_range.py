for x in range(1, 1001):
    fact = 1
    a = x
    total = 0
    while a > 0:
        fact = 1
        rem = a % 10
        for y in range(1, rem+1):
            fact *= y
        total += fact
        a //= 10
    if x == total:
        print(x)
