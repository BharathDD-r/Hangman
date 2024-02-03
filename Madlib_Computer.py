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
        remark = input(f"Is the Number {computer_guess} higer(h), lower(l) or correct(c)? : ")
        if remark == "h":
            higher_limit = computer_guess - 1
        elif remark == "l":
            lower_limit = computer_guess + 1

    print(f"Congragulations you guessed the number {computer_guess} correctly")


computer_find(10)
