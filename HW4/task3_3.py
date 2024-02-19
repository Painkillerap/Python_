


import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def check_multiplicity(amount) -> float:
    while True:
        # amount = int(input("Введите сумму опреации кратно 50\n"))
        if amount % MULTIPLICITY == 0:
            return amount
        else:
            print("Сумма должна быть кратной 50 у.е.")
            break

def deposit(amount):
    check_multiplicity(amount)
    global bank_account
    global count
    bank_account+=amount
    count+=1

    print(f'Пополнение карты на {bank_account} у.е. Итого {amount} у.е.')

def withdraw(amount):
    global bank_account
    global count
    bank_account-=amount
    count+=1
    if amount * PERCENT_REMOVAL < 30:
        bank_account -= 30
        print("списаны проценты за cash: ", 30)
    elif amount * PERCENT_REMOVAL > 600:
        bank_account -= 600
        print("списаны проценты за cash: ", 600)
    else:
        bank_account -= amount * PERCENT_REMOVAL
        print("списаны проценты за cash: ", amount * PERCENT_REMOVAL)
    # if count % 3 == 0:
    #     bank_account = bank_account + percent_add * bank_account
    #     print("начислены проценты в размере: ", percent_add * bank_account)

    print(f'Снятие с карты {amount} у.е. Процент за снятие 60 у.е.. Итого {bank_account} у.е.')



def exit_bank():
    global bank_account
    if bank_account > RICHNESS_SUM:
        bank_account = bank_account - bank_account * RICHNESS_PERCENT
        print("списан налог на богатство: ", bank_account * RICHNESS_PERCENT)
    exit()


deposit(10000)
withdraw(4000)
operations.append(deposit(amount=float), withdraw(amount=float))



# print(check_multiplicity(1000))

# exit()

# print(operations)