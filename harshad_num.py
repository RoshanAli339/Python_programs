n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    sum += temp % 10
    temp //= 10

if n % sum == 0:
    print(n, "is a Harshad or Niven number")
else:
    print(n, "is not a Harshad or Niven number")
