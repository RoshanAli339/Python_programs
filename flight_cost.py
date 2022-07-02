def final_cost(n1, n2):
    cost = 37550*n1 + (37500/3)*n2
    cost += cost * (7/100)
    cost -= cost * (10/100)
    return cost

n_adult = int(input("Enter number of adults: "))
n_child = int(input("Enter number of children: "))
print("Total ticket cost: Rs.", final_cost(n_adult, n_child))
