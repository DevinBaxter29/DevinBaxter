import random

number = random.randint(1, 100)
guess = 0

print("Guess a number 1-100.")

while not guess == number:
    guess = int(input("Guess the number: "))
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")

print("Correct! You win!")
