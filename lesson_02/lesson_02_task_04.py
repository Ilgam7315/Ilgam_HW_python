n = int(input("Введите число:"))


def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)


fizz_buzz(n)

