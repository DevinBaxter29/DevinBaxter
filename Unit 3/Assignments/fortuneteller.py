import random


def visit_fortune_teller():  # Defines function "visit_fortune_teller"
    
    try:
        lucky_num = int(input("Enter a lucky number : "))
        years = float(input("Enter how many years into the future you want to see : "))
        multiplier = float(input("Enter a multiplier number : "))

    except ValueError:
        print("Please enter valid numbers only.")
        return

    cosmic_modifier = random.randint(1, 20)

    destiny_score = (lucky_num * multiplier * years) + cosmic_modifier

    if destiny_score < 25:
        fortune = "You will find something you lost"
    elif destiny_score < 75:
        fortune = "Value your friends over money"
    elif destiny_score < 150:
        fortune = "An exciting trip is coming soon"
    elif destiny_score < 300:
        fortune = "Success is guaranteed in your next step"
    else: destiny_score >= 300
    fortune = "You are destined for greatness"

    print("Your Destiny Score is: " + str(round(destiny_score, 2)))
    print("Your Fortune Is: " + fortune)


visit_fortune_teller()
