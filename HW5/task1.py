# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# def fibonacci(number: int) -> (iter, int):
#     fibo_list = [0, 1, 1]
#     current_number = 0
#     while current_number < number:
#         while len(fibo_list) < number:
#             fibo_list.append(sum(fibo_list[-2:]))
#         yield fibo_list[current_number]
#         current_number += 1





f = fibonacci()
for i in range(10):
    print(next(f))