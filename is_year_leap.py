def is_year_leap(year):
    num = year % 4
    if num == 0:
        return True
    else:
        return False

year = int(input('Введите год для проверки: '))

print(is_year_leap(year))