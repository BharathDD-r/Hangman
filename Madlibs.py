import random


def guess(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    my_guess = 0
    while my_guess != random_number:
        my_guess = int(input(f" guess a number between 1 and {x}: "))
        if my_guess < random_number:
            print("low")
        elif my_guess > random_number:
            print("high")
    print(f"congo you guessed the number {random_number}")


guess(10)
