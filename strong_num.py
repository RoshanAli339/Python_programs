def fact(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

n = int(input('Enter a number: '))

sum = 0
temp = n

while(temp):
    sum += fact(temp % 10)
    temp //= 10

if sum == n:
    print(f"{n} is a Strong number!")