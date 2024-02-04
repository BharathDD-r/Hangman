import random


def game():
    user = input("scissors(s), paper(p) or rock(r) ?: ")
    computer = random.choice(["s", "p", "r"])
    if user == computer:
        print("computer:", computer)
        print("you tied")
    elif win_con(user, computer):
        print("computer:", computer)
        print("you won")
    else:
        print("computer:", computer)
        print("you lose")


def win_con(player, opponent):
    if (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r") \
            or (player == "r" and opponent == "s"):
        return True


game()
