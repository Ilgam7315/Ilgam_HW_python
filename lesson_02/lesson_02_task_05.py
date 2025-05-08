def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "зима"
    elif 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (от 1 до 12): "))
    print(month_to_season(month))
except ValueError:
    print("Введите целое число от 1 до 12!")
