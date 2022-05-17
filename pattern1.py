for i in range(0, 11):
    if i % 5 == 0:
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