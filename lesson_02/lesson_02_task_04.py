n = int(input("Введите число:"))
def fizz_buzz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print(f"FizzBuzz")
        elif num % 5 == 0:
            print(f"Buzz")
        elif num % 3 == 0:
            print(f"Fizz")
        else:
            print(num)
fizz_buzz(n)