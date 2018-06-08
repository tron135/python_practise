print("...rock...")
print("...paper...")
print("...scissors...")
p1 = input("Enter player 1's choice: ")
p2 = input("Enter player 2's choice: ")

if p1 == p2:
	print("It's a draw play again..!!")

elif p1 == "rock":
	if p2 == "paper":
		print("Shoot!!!!")
		print("p2 wins!!!!")

	elif p2 == "scissors":
		print("Shoot!!!!")
		print("p1 wins!!!!")

elif p1 == "paper":
	if p2 == "scissors":
		print("Shoot!!!!")
		print("p2 wins!!!!")

	elif p2 == "rock":
		print("Shoot!!!!")
		print("p1 wins!!!!")

elif p1 == "scissors":
	if p2 == "rock":
		print("Shoot!!!!")
		print("p2 wins!!!!")

	elif p2 == "paper":
		print("Shoot!!!!")
		print("p1 wins!!!!")

else:
	print("something went wrong..!!")


# if p1 == "rock" and p2 == "paper":
# 	print("Shoot!!!!")
# 	print("p2 wins!!!!")
# elif p1 == "rock" and p2 == "scissors":
# 	print("Shoot!!!!")
# 	print("p1 wins!!!!")

# elif p1 == "paper" and p2 == "scissors":
# 	print("Shoot!!!!")
# 	print("p2 wins!!!!")
# elif p1 == "paper" and p2 == "rock":
# 	print("Shoot!!!!")
# 	print("p1 wins!!!!")

# elif p1 == "scissors" and p2 == "rock":
# 	print("Shoot!!!!")
# 	print("p2 wins!!!!")
# elif p1 == "scissors" and p2 == "paper":
# 	print("Shoot!!!!")
# 	print("p1 wins!!!!")

# elif p1 == p2:
# 	print("It's a draw play again..!!")
# else:
# 	print(something went wrong..!!)