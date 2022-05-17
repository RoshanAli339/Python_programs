n = int(input('Enter a number: '))

sum = 1

for i in range(2,n):
    if n % i == 0:
        sum += i

if sum == n:
    print(f"{n} is a perfect number!")
elif sum > n:
    print(f"{n} is an efficient number!")
else:
    print(f"{n} is a deficient number!")