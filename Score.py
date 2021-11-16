import Utils


def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
            try:
                with open(Utils.SCORES_FILE_NAME, 'w') as file:
                    file.write(str(current_score + (difficulty * 3) + 5))
            except:
                raise Exception('Could not write to  Scores.txt')
    except:
        print('Could not open Scores.txt. Creating new one.')
        try:
            with open(Utils.SCORES_FILE_NAME, 'w') as file:
                file.write(str((difficulty * 3) + 5))
        except:
            raise Exception('Could not write to  Scores.txt')


def create_zero_score():
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    except:
        print('Could not open Scores.txt. Creating new one with zero value.')
        try:
            with open(Utils.SCORES_FILE_NAME, 'w') as file:
                file.write("0")
        except:
            print('Could not write to Scores.txt.')
