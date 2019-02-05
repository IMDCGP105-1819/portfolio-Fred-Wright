from random import randint
random_number = randint(0,100)

print("Make a guess")
guess = int(input())

number_of_guesses = 0

while guess != random_number:
    if guess < random_number:
        print("Too low")
        print("Make another guess")
        guess = int(input())
        number_of_guesses = number_of_guesses + 1
    elif guess > random_number:
        print("Too high")
        print("Make another guess")
        guess = int(input())
        number_of_guesses = number_of_guesses + 1
else:
    print("Perfect, you did it in:", number_of_guesses, "guesses!")
