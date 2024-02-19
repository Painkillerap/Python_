# import random
#
# def is_safe(board, row, col):
#     for i in range(row):
#         if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
#             return False
#     return True
#
# def generate_boards():
#     board = [-1] * 8
#     for i in range(8):
#         while True:
#             col = random.randint(0, 7)
#             if is_safe(board, i, col):
#                 board[i] = col
#                 break
#     return board
#
# board_list = []
# for _ in range(4):
#     board_list.append(generate_boards())
# board_list
# print(generate_boards())


import random
from itertools import combinations

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list