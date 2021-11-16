import random
from time import sleep
from Utils import Screen_cleaner

difficulty = 3
random_list = []


def generate_sequence():
    global random_list
    for index in range(0, difficulty):
        random_list.append(random.randint(1, 101))


def get_list_from_user():
    guess_list = []
    for index in range(1, difficulty + 1):
        no_exception = False
        while not no_exception:
            print("Please type your guess number by number - " + str(index) + " number: ")
            try:
                user__guess = int(input(">>>"))
                if user__guess not in range(1, 101):
                    raise ValueError
                else:
                    no_exception = True
            except ValueError as e:
                print("\t\tOnly numbers between 1 to 101 are allowed!\n")
        guess_list.append(user__guess)
    return guess_list


def is_list_equal():
    random_list1 = set(random_list)
    print("You chose memory Game. Try to memorize the following set of numbers: ")
    print(random_list1)
    sleep(3)
    print("\n" * 100)
    Screen_cleaner()
    random_list2 = set(get_list_from_user())
    print("The numbers were: " + str(random_list1) + ", you entered numbers : " + str(random_list2) + ".")
    if len(random_list1 & random_list2) == int(difficulty):
        return True
    return False


def play():
    generate_sequence()
    return is_list_equal()


def set_difficulty(difficulty_value):
    global difficulty
    difficulty = difficulty_value
