n = int(input("Enter a number: "))
m = n ** 3

if m % (10**len(str(n))) == n:
    print(n, " is a Trimotrphic number")
    
