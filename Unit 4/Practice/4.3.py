import random

number = random.randint(1,2)
guess = input("Guess the number.\n> ")
while guess == number:
    print("Correct")

else:
    print("Incorrect")
    guess = input("Guess the number.\n> ")