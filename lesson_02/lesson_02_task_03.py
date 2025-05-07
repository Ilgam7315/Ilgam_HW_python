import math


def square(n):
    return math.ceil(l_side * l_side)


l_side = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(l_side)}")
