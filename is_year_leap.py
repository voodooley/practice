def is_year_leap(year):
    num = year % 4
    if num == 0:
        return True
    else:
        return False


def is_year_leap2(ye):
    return not bool(ye % 4)


year = int(input('Введите год для проверки: '))

print(is_year_leap(year))

year2 = int(input('Введите год2 для проверки: '))
print(is_year_leap2(year2))