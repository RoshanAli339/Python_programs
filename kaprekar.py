n = int(input("Enter a number: "))
l = len(str(n**2))
f = 0
a3 = 0
a4 = 0
if l % 2 == 0:
    a1 = (n**2) % (10**(l/2))
    a2 = (n**2) // (10**(l/2))
else:
    a1 = (n**2) % (10**((l+1)//2))
    a2 = (n**2) // (10**((l+1)//2))
    a3 = (n**2) % (10**((l-1)//2))
    a4 = (n**2) // (10**((l-1)//2))
f = a1 + a2
f1 = a3 + a4
if f == n or f1 == n:
    print(f"{f}  {f1}  {a1}  {a2}  {a3}  {a4}")
    print(n, " is a Kaprekar number")
else:
    print(n, " is not a Kaprekar number")