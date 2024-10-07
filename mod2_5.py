def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return (matrix)

n = int(input("количество строк "))
m = int(input("количество стобцов "))
value = input("значение ")
matrix = get_matrix(n,m,value)

if n <= 0:
    print("неверное количество строк:", n)
elif m <=0:
    print("неверное количество столбцов:" ,m)
else:
    print("Матрица:")
    for i in matrix:
        print(*i)