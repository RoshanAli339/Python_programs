def get_cents():
    n = 0
    while True:
        n = int(input("Enter number of cents: "))
        if n >= 0:
            break
    return n

def calculate_pennies(cents):
    return cents

def calculate_nickels(cents):
    return cents // 5

def calculate_dimes(cents):
    return cents // 10

def calculate_quarters(cents):
    return cents // 25

cents = get_cents()

quarters = calculate_quarters(cents)
cents -= quarters * 25

dimes = calculate_dimes(cents)
cents -= dimes * 10

nickles = calculate_nickels(cents)
cents -= nickles * 5

pennies = calculate_pennies(cents)
cents -= pennies

coins = pennies + nickles + dimes + quarters

print(f"{coins}")
