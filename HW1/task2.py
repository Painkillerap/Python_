# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
#
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
#def is_prime(num):
# if (num <= 1 or num > 100000):
#     print("Не является простым")
# if num == 2:
#     print("Простое")
# if num % 2 == 0:
#     print("Не является простым")
# for i in range(3, int(num**0.5)+1, 2):
#     if num % i == 0:
#         print("Не является простым")
#     print("Простое")

# if (num <= 1 or num > 100000):
#     print("Не является простым")
# if num == 2:
#      print("Простое")
# for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#         print("Не является простым")
#     print("Простое")

num=-1
k = 0
if (num <= 1 or num > 100000):
    print("Число должно быть больше 1 и меньше 100000")
else:
    for i in range(2, num // 2+1):
        if (num % i == 0):
            k = k+1
    if (k <= 0):
        print("Простое")
    else:
        print("Число не является простым")