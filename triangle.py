def is_triangle(a, b, c):
    if a+b < c or b+c < a or a+c < b:
        print('No')
    else:
        print('Yes')

def prompt():
    a = int(input('Enter length of first stick: '))
    b = int(input('Enter length of second stick: '))
    c = int(input('Enter length of third stick: '))

    print('Do the three sticks form a triangle?: ',end=' ')
    is_triangle(a, b, c)

prompt()