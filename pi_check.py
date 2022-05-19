import math

def estimate_pi():
    sum = 0
    val = 0
    k = 0
    while True:
        val = ( math.factorial(4 * k) * (1103 + 26390 * k) ) / ( math.factorial(k) * (396)**(4 * k))
        if val < 1e-15:
            break

        sum += val
        k += 1
    
    sum = sum * ( 2 * math.sqrt(2) / 9801)

    if sum == 1/math.pi:
        print('Theory is correct')
    else:
        print('Theory is wrong')

estimate_pi()