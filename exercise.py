def cube(num):
    return num**3

def by_three(num):
    if num%3 == 0:
        return cube(num)
    else:
        return 'false'

a = input('Enter a number: ')
if a.isnumeric():
    print(by_three(int(a)))
else:
    print('Given input is not a number')
