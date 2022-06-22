def scholarship_Calc(branch, score, fee):
    sc = 0.0
    if branch == 'Arts':
        if score >= 90 and score % 2 != 0:
            sc = fee * (50/100)
        elif score % 2 != 0:
            sc = fee * (5/100)
    elif branch == 'Engineering':
        if score >= 85 and score % 7 != 0:
            sc = fee * (50/100)
        elif score % 7 == 0:
            sc = fee * (5 / 100)
    return fee - sc

n = int(input("Enter number of students: "))
print(f"Enter the details of {n} students: ")

for i in range(n):
    branch = input("Enter branch of study: ")
    while branch != 'Arts' and branch != 'Engineering':
        branch = input("Enter branch of study: ")
    score = int(input("Enter score in entrance exam: "))
    fee = float(input("Enter fee for the given branch: "))
    print("Final fee to be paid by the student is: Rs.", scholarship_Calc(branch, score, fee))
