import math

def square_root(a, x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y

def test_square_root():
    i = 1.0
    while i < 11.0:
        msqrt = square_root(i, i/2)
        difference = abs(msqrt - math.sqrt(i))
        print(f'{i}\t\t{msqrt}\t\t{math.sqrt(i)}\t\t{difference}')
        i += 1.0

test_square_root()