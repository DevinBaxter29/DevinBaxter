import random
wallet = 0
dishes_done = False
hands_washed = False
showered = False

def start():
    
    print("Welcome to Life")
    print("You stand at the entrance of your home. Do you:")
    print("1. Enter your house")
    print("2. Go to neighbor's pool")
    print("3. Go to your backyard")

    choice = input("> ")

    if choice == "1":
        enter_house()
    elif choice == "2":
        go_neighbors_pool()
    elif choice == "3":
        backyard()
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

def backyard():
    print("You enter your backyard")
    print("1. Go Swimming")
    print("2. Sunbathe")
    print("3. Enter Shed")
    print("4. Go Back")

    choice = input("> ")

    if choice == "1":
        swim()
    elif choice == "2":
        sunbathe()
    elif choice == "3":
        shed_outside()
    elif choice == "4":
        start()
    
def shed_outside():
    print("As you get close to the shed you hear a noise")
    print("1. Enter")
    print("2. Go Back")

    choice = input("> ")

    if choice == "1":
        shed_inside()
    elif choice == "2":
        backyard()
    else:
        print("Invalid Choice. Try Again")
        shed_outside()

def shed_inside():
    print("You open the shed and racoon jumps at you")
    print("1. Shut the door")
    print("2. Run")

    choice = input("> ")

    if choice == "1":
        shut()
    elif choice == "2":
        run()
    else:
        print("Invalid Choice. Try Again")
        shed_inside()

def shut():
    print("As you try to shut the door")
    shut = random.randint(1,3)

    if shut == 2:
        print("You managed to shut the door just in time")
    elif 1 or 3:
        print("You couldn't shut it in time")
        print("Ending 5: You Got Mauled by a racoon")

def run():
    print("You decide to run inside")
    print("You made it")
    bedroom()



def swim():
    print("You Approach the Edge of the Pool")
    print("1. Jump into The water")
    print("2. Take the Stairs in the Pool")
    print("3. Go back")

    choice = input("> ")

    if choice == "1":
        print("You jump into the water and then you get out")
        global showered 
        showered = False
        swim()
    elif choice == "2":
        print("As you take the stairs you slip")
        print("Ending 4: You hit your head")
    elif choice == "3":
        backyard()
    else:
        print("Invalid Choice. Try Again")
        swim()

def go_neighbors_pool():
    print("You Sneak into your neighbors yard.")
    print("They catch you and you go to prison for 12 years")
    print("Ending 1: You got caught")

def kitchen():
    print("1. Open Fridge")
    print("2. Do the Dishes")
    print("3. Wash your Hands")

    global hands_washed
    global dishes_done

    choice = input("> ")

    if choice == "1":
        if hands_washed == True and dishes_done == True:
            open_fridge()
        else:
            print("Your chores are not done")
            kitchen()
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
    print("You have 2 Cheeses, 2 types of sandwhich meats, and 1 condiment")
    print("1. Swiss,Ham,Mayo")
    print("2. Swiss,Turkey,Mayo")
    print("3. American,Ham,Mayo")
    print("4. American,Turkey,Mayo")
    print("5. Deicde not to eat")

    choice = input("> ")

    if choice == "1":
        print("You made a Ham,Swiss,Mayo Sandwhich")

    elif choice == "2":
        print("You made a Turkey,Swiss,Mayo Sandwhich")

    elif choice == "3":
        print("You made a Ham,American,Mayo Sandwhich")

    elif choice == "4":
        print("You made a Turkey,American,Mayo Sandwhich")

    elif choice == "5":
        print("You Have Decided to Starve")
        print("Ending 3: You Have Starved")
    else:
        print("Invalid Choice. Try Again")
        open_fridge()

def sleep():
    print("You were to tired to make food")
    print("Ending 2: Go to Sleep")

def shower():
    print("You Chose to Shower")
    print("You Feel clean now")

    global showered
    showered = True

    print("1. Leave Bathroom")

    choice = input("> ")

    if choice == "1":
        start()
    else:
        print("Invalid Choice. Try Again")
        shower()
        
def make_bed():
    global wallet

    print("You look at your messy bed and decide to make it look nice")

    cash_found = random.randint(1, 20)

    print("You found ","$",cash_found, "while making your bed")

    wallet += cash_found

    print("You Have: $",wallet)
    print("1. Leave Bedroom")

    choice = input("> ")

    if choice == "1":
        start()
    else:
        print("Invalid Choice. Try Again")
        make_bed()

def do_dishes():
    print("You look at the full sink and decide to do dishes")

    global dishes_done 
    dishes_done = True

    print("1. Leave Kitchen")
    print("2. Wash Hands")

    choice = input("> ")

    if choice == "1":
        start()
    elif choice == "2":
        wash_hands()
    else:
        print("Invalid Choice. Try Again")
        do_dishes()

def wash_hands():
    print("You wash your hands.")
    print("1. Leave Kitchen")

    global hands_washed
    hands_washed = True

    choice = input("> ")

    if choice == "1":
        start()
    else:
        print("Invalid Choice. Try Again")
        wash_hands()

start()