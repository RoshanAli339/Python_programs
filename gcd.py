def gcd(a, b):
    if b == 0:
        return a
    elif a > 0  and b > 0:
        return gcd(b, a%b)

a = int(input('Enter value of A: '))
b = int(input('Enter value of B: '))

print('GCD= ', gcd(a, b))
