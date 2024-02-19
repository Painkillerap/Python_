# date_to_prove = '0.5.2022'
date_to_prove = '12.5.-2022'




def is_valid_date(date):
    format = "%d.%m.%Y"
    try:

        day, month, year = map(int, date.split('.'))
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True
    except ValueError:
        return False


print(is_valid_date(date_to_prove))

from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))
