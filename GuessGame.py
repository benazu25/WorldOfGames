import random

difficulty = 3
secret_number = 0


def generate_number():
    global secret_number
    secret_number = random.randint(1, difficulty)


def get_guess_from_user():
    no_exception = False
    while not no_exception:
        print("You chose Guess Game. The system randomly chose a number between 1 and " + str(difficulty) +
              ". \nPlease type your guess (Number between 1 and " + str(difficulty) + "): ")
        try:
            user__guess = input(">>>")
            if int(user__guess) not in range(1, difficulty + 1):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print(f"\t\tOnly Numbers between 1 to {difficulty} are allowed!\n")
    return int(user__guess)


def compare_results():
    guess_from_user = get_guess_from_user()
    print("System chose number " + str(secret_number) + ", you entered number " + str(guess_from_user) + ".")
    return secret_number == guess_from_user


def play():
    generate_number()
    return compare_results()


def set_difficulty(difficulty_value):
    global difficulty
    difficulty = difficulty_value
