#taking a number input and checking if it is in between 1 and 8
n = 0
while True:
    n = int(input("Enter a number: "))

    #checking if n is >=1 and <=8
    if n >= 1 and n <= 8:
        break

#looping through n times
for i in range(n+1):
    for j in range(i, n):
        print(" ",end='')
    for j in range(i):
        print("#",end='')
    print()

