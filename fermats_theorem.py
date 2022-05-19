a = int(input('Enter value of A: '))
b = int(input('Enter value of B: '))
c = int(input('Enter value of C: '))
n = int(input('Enter value of N: '))

if (a**n + b**n) == c**n and n > 2:
    print('Holy smokes, Fermat was wrong')
else:
    print('No, that doesn\'t worK!')
    