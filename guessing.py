import random

random_number = random.randint(1,10)

while True:
	guess = input("Guess a number between 1 to 10: ")
	if int(guess) < random_number:
		print("Your number is too low..!! Try again..!!")
	elif int(guess) > random_number:
		print("Your number is too high..!! Try again..!!")
	else:
		print("Congrats..!! You have guessed right number..!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
		break