matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]



# def transpose(matrix):
#     trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]  # структура транспонированной матцы
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             trans_matrix[j][i] = matrix[i][j]
#     return trans_matrix



def transpose(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return trans_matrix


print(transpose(matrix))

def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed