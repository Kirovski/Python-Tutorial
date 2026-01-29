import random
print("Guess my number between 1 and 20")
realNumber = random.randint(1,21)
print(realNumber)
userGuess =int(input('>'))

while userGuess != realNumber:
	print("Wrong! Try again!")
	userGuess = int(input('>'))
print("You guessed it correctly")

