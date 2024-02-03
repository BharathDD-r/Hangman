import random


def computer_find(x):
    lower_limit = 1
    higher_limit = x
    remark = ""
    while remark != "c":
        if lower_limit != higher_limit:
            computer_guess = random.randint(lower_limit, higher_limit)
        else:
            computer_guess = higher_limit
        remark = input(f" is {computer_guess} (h) (l) or (c)?: ")
        if remark == "h":
            higher_limit = computer_guess - 1
        elif remark == "l":
            lower_limit = computer_guess + 1

    print(f" congo you guessed the number correctly")


computer_find(10)
