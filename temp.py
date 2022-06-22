temp = float(input("Enter temperature: "))
units = input("Enter units C(Celcius) or F(Farenhiet): ")
ftemp = 0

if units == 'C' or units == 'c':
    ftemp = (temp * (9/5))+ 32
    print(ftemp, "F")
elif units == 'F' or units == 'f':
    ftemp = (temp - 32) * (5/9)
    print(ftemp, "C")
else:
    print("Invalid units!")
