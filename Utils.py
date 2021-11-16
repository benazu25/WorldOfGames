import os


SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


def Screen_cleaner():
    os.system("cls")


def Pause_cmd():
    os.system("pause")


def run_flask():
    os.system("python MainScores.py")


def define_BAD_RETURN_CODE(BAD_RETURN_CODE_value):
    global BAD_RETURN_CODE
    BAD_RETURN_CODE = BAD_RETURN_CODE_value
