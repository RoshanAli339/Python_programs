n = int(input("Enter a number: "))

temp = n
sum = 0
for i in range(len(str(n)), 0, -1):
    sum += (temp%10) ** i
    temp //= 10

if sum == n:
    print(n, " is a Disarium number")
else:
    print(n, " is not a Disarium number")
