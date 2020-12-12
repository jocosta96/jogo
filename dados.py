import random


def welcome():
    print("******************************")
    print("*Welcome to dice rolling game*")
    print("******************************")
    print("v0.1.0")


def ask():
    quantity = int((input("How many dices do you want to use? ").strip()))
    return quantity


def game_loop():
    index = 1
    total_score = 0
    quantity = ask()

    while index <= quantity:
        single_score = random.randrange(1, 7)
        print("In round {} you´re reached the number {}".format(index, single_score))
        total_score += single_score
        index += 1
    print("Your total score is {}".format(total_score))


def gameplay():
    welcome()
    game_loop()


if __name__ == "__main__":
    gameplay()
