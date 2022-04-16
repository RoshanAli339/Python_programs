m = int(input('Enter number of rows: '))
n = int(input('Enter number of columns: '))

mat = [None]*m;
for i in range(n):
    mat[i] = [None]*n;

print("Enter the elements of the matrix: ")
for i in range(m):
    print(f"Enter the elements of rows {i}: ")
    ele = input()
    mat[i] = ele.split()
    for j in range(n):
        mat[i][j] = int(mat[i][j])

print("The elements of the matrix are: ")
for i in range(m):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()


