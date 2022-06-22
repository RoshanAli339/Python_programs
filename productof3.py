ele = input("Enter three numbers: ")
a = ele.split(' ')
a = [int(x) for x in a]

mul = 1
if 7 in a:
    if a.index(7) == 2:
        mul = -1
    elif a.index(7) == 1:
        mul = a[2]
    else:
        mul = a[1] * a[2]
else:
    mul = a[0] * a[1] * a[2]

print("Multiplication: ", mul)
