n = int(input("Enter a number: "))
m = n ** 2

if m % (10**len(str(n))) == n:
        print(n, " is an Automorphic number")
else:
        print(n, "is not an Automorhic number")
        
