day = int(input('Введите число рождения: '))

month = str(input('Введите   месяц  рождения: '))

if month == 'декабрь' and day >= 22 or month == 'январь' and day <= 19:
    print(f"{month} {day} -> Козерог")
elif month == 'январь' and day >= 20 or month == 'февраль' and day <= 18:
    print(f"{month} {day} -> Водолей")
elif month == 'февраль' and day >= 19 or month == 'март' and day <= 20:
    print(f"{month} {day} -> Рыбы")