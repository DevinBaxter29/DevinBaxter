import random

number = random.randint(1, 100)
guess = 0
count = 0
print("Guess a number 1-00.")

while not guess == number:
    guess = int(input("Guess the number: "))
    count += 1
    if guess < number:
        print("Too low! Try again.")
        
    elif guess > number:
        print("Too high! Try again.")

print("Correct! You win!")
print("You guessed " + str(count),"Times")

if count == 1:
    print("You got Unreal")
elif count <=3:
    print("You got Champion")
elif count <=5:
    print("You got Elite")
elif count <=7:
    print("You got Dimond")
elif count <=9:
    print("You got Platinum")
elif count <=11:
    print("You got Gold")
elif count <=13:
    print("You got Silver")
elif count >=15:
    print("You Got Bronze")
else:
    print("You got Wood")

#1 is unreal
#2-3 is champion
#4-5 is elite
#6-7 is dimond
#8-9 is platinum
#10-11 is gold
#12-13 is silver
#14-15 is bronze
#>15 is wood