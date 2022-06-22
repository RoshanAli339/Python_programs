def sum_fact(n):
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0: sum += i
    return sum

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if sum_fact(n1) == n2 and sum_fact(n2) == n1:
    print(f"{n1}, {n2} is an Amicable pair")
else:
    print(f"{n1}, {n2} is not an Amicable pair")
