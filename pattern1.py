for i in range(0, 11):
    if i == 0 or i == 5 or i == 10:
        for j in range(0, 11):
            if j %  5 == 0:
                print('+',end=' ')
            else:
                print('-',end=' ')
    else:
        for j in range(0, 11):
            if j % 5 == 0:
                print('|',end=' ')
            else:
                print(' ',end=' ')
    print('\n')