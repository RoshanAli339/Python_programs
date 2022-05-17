import math

n = int(input('Enter a number: '))

sum = 0
l = 0
temp = n

while(temp):
    l += 1
    temp //= 10

temp = n
while (temp):
    sum += math.pow(temp%10, l)
    temp //= 10

if sum == n:
    print(f"{n} is an Armstrong number!")