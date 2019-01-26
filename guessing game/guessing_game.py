from random import randint
import datetime
import os


def game():
	while True:
		computer_guess = randint(1, 100)
		result = guess(computer_guess)

		record_score(result)

		if input("want to continue? ").lower() == 'n':	#in order ro exit press anything except 'n'
			break


def record_score(current_score_and_date):
	print(current_score_and_date)
	try:
		score_record = open("score_record.txt", 'a')
		high_score = open("high_score.txt", 'r')

	except FileNotFoundError:
		print("File is missing. Better create it")

	else:
		score_record.write("\n" + current_score_and_date)

		#if file doesn't have any score
		if os.stat("high_score.txt").st_size == 0:
			high_score.write(current_score_and_date)

		else:
			current_high_score_and_date = high_score.read()

			if int(current_score_and_date.split("		")[0]) > int(current_high_score_and_date.split("		")[0]):
				high_score.close()
				high_score = open("high_score.txt", 'w')	#because r+ is not working
				high_score.write(current_score_and_date)

	finally:
		score_record.close()
		high_score.close()


#record_score(256, datetime.datetime.now())


def guess(computer_guess):
	guess_counter = 50

	while guess_counter > 0:

		print("chances left {}" .format(guess_counter))
		user_choice = int(input("guess the number: "))

		print("\n\n ------------------------------------------ \n\n")
		if user_choice > computer_guess:
			print("you are a bit too high...")

		elif user_choice < computer_guess:
			print("you are a bit too low...")

		else:
			print("bravo! you guessed the number.")
			break

		guess_counter -= 1

	return "{}		{}" .format(guess_counter, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


game()
