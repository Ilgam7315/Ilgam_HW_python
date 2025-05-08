def is_year_leap(number):
    return number % 4 == 0


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"год {num}: - {result}")

# вместо return True if number % 4 == 0 else False можно
# сократить и написать: return number % 4 == 0

