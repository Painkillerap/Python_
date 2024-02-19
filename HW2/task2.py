# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.
import fractions
def process_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    # Вычисляем сумму дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляем произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

# Пример использования функции
frac1 = "1/2"
frac2 = "1/3"

sum_frac, prod_frac = process_fractions(frac1, frac2)

print(f"Сумма дробей: {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей: {prod_frac[0]}/{prod_frac[1]}")

def calculate_fraction_sum_and_product(frac1, frac2):
    a1, b1 = frac1.split('/')
    a2, b2 = frac2.split('/')
    frac1 = fractions.Fraction(int(a1), int(b1))
    frac2 = fractions.Fraction(int(a2), int(b2))

    sum_frac = frac1 + frac2
    mul_frac = frac1 * frac2

    sum_numerator = sum_frac.numerator
    sum_denominator = sum_frac.denominator

    mul_numerator = mul_frac.numerator
    mul_denominator = mul_frac.denominator

    return sum_numerator, sum_denominator, mul_numerator, mul_denominator

sum_frac_1 = calculate_fraction_sum_and_product(frac1, frac2)

print(f"Сумма дробей: {sum_frac_1[0]}/{sum_frac_1[1]}")
print(f"Произведение дробей: {sum_frac_1[2]}/{sum_frac_1[3]}")


