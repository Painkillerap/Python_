# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.


from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("списаны проценты за cash: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны проценты за cash: ", 600)
    else:
        bank -= cash * percent_take
        print("списаны проценты за cash: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()