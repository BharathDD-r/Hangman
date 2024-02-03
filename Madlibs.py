import random


def guess(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    my_guess = 0
    while my_guess != random_number:
        my_guess = int(input(f"Please guess a number between 1 and {x}: "))
        if my_guess < random_number:
            print(f"The number {my_guess} is lower than the guess")
        elif my_guess > random_number:
            print(f"The number {my_guess} is higher than the guess")
    print(f"Congratulations you have guessed the number {random_number} correctly!")


guess(10)
