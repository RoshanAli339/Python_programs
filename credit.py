def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10

    return sum

cardno = input("Enter the credit card number: ")
numbers = [int(i) for i in cardno]

sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        if 2 * numbers[i] > 9:
            sum += sum_digits(2 * numbers[i])
        else:
            sum += 2 * numbers[i]
    else:
        sum += numbers[i]
print(f"Sum= {sum}")
if sum % 10 == 0 and len(numbers) >= 13 and len(numbers) <= 16:

    am  = numbers[0] * 10 + numbers[1]
    if len(numbers) == 15 and (am == 34 or am == 37):
        print("AMEX")
    
    elif len(numbers) == 15 and (am == 51 or am == 52 or am == 53 or am == 54 or am == 55):
        print("MASTERCARD")

    elif (len(numbers) == 13 or len(numbers) == 16) and numbers[0] == 4:
        print("VISA")

    else:
        print("INVALID")
else:
    print("INVALID")

