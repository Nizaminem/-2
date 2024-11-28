def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        row = []
        for a in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
res_matrix = get_matrix(int(input("Введите количество строк: ")),
                        int(input("Введите количество столбцов: ")),
                        int(input("Введите нужную цифру: ")))
#res_matrix = get_matrix(2,2,10)
print(res_matrix)

