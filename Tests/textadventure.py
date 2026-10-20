print("Welcome to Life")

def start():
    print("You stand at the entrance of your home. Do you:")
    print("1. Enter your house")
    print("2. Go to a pool")

    choice = input("> ")

    if choice == "1":
        enter_house()
    elif choice == "2":
        go_pool()
    else:
        print("Invalid choice. Try again.")
        start()

def enter_house():
    print("You decide to enter your home.")
    print("You stand right inside your house. As you put your hat and jacket away you start to get hungry")
    print("1. Go to Kitchen")
    print("2. Go to Bedroom")
    print("3. Go to Bathroom")

    choice = input("> ")

    if choice == "1":
        kitchen()
    elif choice == "2":
        bedroom()
    elif choice == "3":
        bathroom()
    else:
        print("Invalid Choice. Try Again")
        enter_house()

def go_pool():
    print("You decide to go to a pool to swim. You forgot you didn't know how to swim.")
    print("Ending 1: You Drowned")

def kitchen():
    print("1. Open Fridge")
    print("2. Do the Dishes")
    print("3. Wash your Hands")

    choice = input("> ")

    if choice == "1":
        open_fridge()
    elif choice == "2":
        do_dishes()
    elif choice == "3":
        wash_hands()
    else:
        print("Invalid Choice. Try Again")
        kitchen()

def bedroom():
    print("1. Make Bed")
    print("2. Go to Sleep")

    choice = input("> ")

    if choice == "1":
        make_bed()
    elif choice == "2":
        sleep()
    else:
        print("Invalid Choice. Try Again")
        bedroom()

def bathroom():
    print("1. Take a Shower")
    
    choice = input("> ")

    if choice == "1":
        shower()
    else:
        print("Invalid Choice. Try Again")
        bathroom()

def open_fridge():
    print("You have decided to open the fridge")
    print("You have 3 Cheeses, 2 types of sandwhich meats, and 3 condiments")
    #Not Done
def sleep():
    print("You were to tired to make food")
    print("Ending 2: Go to Sleep")

def shower():
    print("You Chose to Shower")
    #Not Done