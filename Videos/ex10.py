number = 0
for number in range(0, 100, 1):
    if number % 3 == 0:
        print("Fizz", number)
    if number % 5 == 0:
        print("Buzz", number)
    if number % 15 == 0:
        print("FizzBuzz", number)
    else:
        print(number)
