import datetime
import os
from pathlib import Path
from random import randint


# TODO include other option like score board etc here.


def game():
    while True:
        computer_guess = randint(1, 100)
        result = guess(computer_guess)

        print("The number was {}".format(computer_guess))

        record_score(result)

        # in order ro exit press anything except 'n'
        try:
            if input("Play again? ").lower() == 'n':
                break
        except ValueError:
            print("you pressed some value. Considered default value NO")
            break


def record_score(current_score_and_date):
    print("\n\n--------------- Game Over ---------------\n\n")
    print("Your Score is " + current_score_and_date.split()[0])

    # if file doesn't exists
    if not Path("score_record.txt").is_file():
        with open('score_record.txt', 'w') as score_record:
            score_record.write(current_score_and_date)

    # following code will ensure that only last 10 results are saved
    with open('score_record.txt', 'r') as score_record:
        all_scores_in_the_record = score_record.readlines()

    all_scores_in_the_record.insert(0, current_score_and_date + '\n')

    if len(all_scores_in_the_record) > 10:
        with open('score_record.txt', 'w') as score_record:
            for item in all_scores_in_the_record[:10]:
                score_record.write(item)

    else:
        with open('score_record.txt', 'w') as score_record:
            for item in all_scores_in_the_record:
                score_record.write(item)

    # if file doesn't exists
    if not Path("high_score.txt").is_file():
        with open('high_score.txt', 'w') as high_score:
            high_score.write(current_score_and_date)
            return None

    if os.stat('high_score.txt').st_size == 0:
        with open('high_score.txt', 'w') as high_score:
            high_score.write(current_score_and_date)
            return None

    with open('high_score.txt', 'r') as high_score:
        current_high_score_and_date = high_score.read()

    if int(current_score_and_date.split()[0]) > int(current_high_score_and_date.split()[0]):
        with open('high_score.txt', 'w') as high_score:
            high_score.write(current_score_and_date)


def guess(computer_guess):
    guess_counter = 10

    while guess_counter > 0:

        try:
            print("chances left {}".format(guess_counter))
            user_choice = int(input("guess the number: "))

            print("\n\n------------------------------------------\n\n")
            if user_choice > computer_guess:
                print("your guess is high")

            elif user_choice < computer_guess:
                print("your guess is low...")

            else:
                print("bravo! you guessed the number.")
                break

            guess_counter -= 1

        except ValueError:
            continue

    return "{}		{}".format(guess_counter, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


game()
