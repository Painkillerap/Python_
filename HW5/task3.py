# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.
import decimal

names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

salary = [7500, 8000, 9000]
bonus = ["8%", "12%", "7%"]


# def premium(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
#     return {name: money / 100 * perc
#             for name, money, perc in zip(names, cash, (float(i[:-1]) for i in  percent))}

def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * float(bonus.strip('%')) / 100 for name, salary, bonus in
            zip(names_list, salaries_list, bonuses_list)}


salary_dict = generate_salary_dict(names, salary, bonus)
print(salary_dict)


result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)
