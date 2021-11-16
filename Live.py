import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Score


def welcome(name):
    return "\nHello " + name + " and welcome to the world of Games (WoG). \nHere you can find many cool games to play\n"


def load_game():
    no_exception = False
    while not no_exception:
        print("Please choose a game to play: \n"
              "\t1. Memory Game - a sequence of  numbers  will appear for 1 second and you have to guess it back \n"
              "\t2. Guess Game - guess a number and see if you  chose like the computer \n"
              "\t3. Currency  Roulette - try and guess the value of a random amount of USD in ILS")
        try:
            user__game_choice = int(input(">>>"))
            if user__game_choice not in range(1, 4):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print("\t\t Only numbers 1, 2 and 3 are allowed!\n")

    no_exception = False
    while not no_exception:
        print("Please choose game difficulty from 1 to 5:")
        try:
            user__difficulty_choice = int(input(">>>"))
            if user__difficulty_choice not in range(1, 6):
                raise ValueError
            else:
                no_exception = True
        except ValueError as e:
            print("\t\t Only numbers from 1 to 5 are allowed!\n")

    if user__game_choice == 2:
        GuessGame.set_difficulty(user__difficulty_choice)
        result = GuessGame.play()
    elif user__game_choice == 1:
        MemoryGame.set_difficulty(user__difficulty_choice)
        result = MemoryGame.play()
    elif user__game_choice == 3:
        CurrencyRouletteGame.set_difficulty(user__difficulty_choice)
        result = CurrencyRouletteGame.play()

    if result == True:
        print("You WON!")
        Score.add_score(user__difficulty_choice)
    else:
        print("You LOST!")
        Score.create_zero_score()
