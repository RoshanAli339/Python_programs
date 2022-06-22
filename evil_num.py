def to_bin(n):
    bin = 0
    i = 0

    while n != 0:
        bin += (n % 2) * (10 ** i)
        i += 1
        n //= 2

    return bin

n = int(input("Enter a number: "))
b = to_bin(n)

c = 0
for i in str(b):
    if i == '1':
        c += 1

if  c % 2 == 0:
    print(n, " is an Evil number")
else:
    print(n, " is an Odious number")
