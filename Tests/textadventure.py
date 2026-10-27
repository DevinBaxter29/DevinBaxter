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
        print("Invalid choice. Try again.\n")
        start()


def enter_house():
    print("You decide to enter your home.")
    print("You stand right inside your house. As you put your hat and jacket away you start to get hungry.")
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
        print("Invalid Choice. Try Again\n")
        enter_house()


def backyard():
    print("You enter your backyard.")
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
    else:
        print("Invalid Choice. Try Again\n")
        backyard()


def sunbathe():
    print("As you sit down a ball comes straight for your face.")
    print("1. Try to block it")
    print("2. Catch it")
    print("3. Don't React")
    
    choice = input("> ")
    if choice == "1":
        block()
    elif choice == "2":
        print("You extend your hands to catch the ball...")
        catch_chance = random.randint(1, 5)
        if catch_chance == 2:
            print("You caught it right out of the air.")
            print("1. Bring the ball inside")
            print("2. Throw it back over your fence")
            print("3. Just leave it")
            
            choice = input("> ")
            if choice == "1":
                print("You pick up the ball and walk inside to put it away.")
                bedroom()
            elif choice == "2":
                print("The ball lands on the other side.")
                backyard()
            elif choice == "3":
                print("You leave the ball sitting on the grass.")
                backyard()
            else:
                print("Invalid Choice.\n")
                backyard()
        else:
            print("The ball slips right through your fingers and hits your face.")
            print("Ending 8: You have been knocked out")
    elif choice == "3":
        print("You just sit there and stare.")
        print("The ball hits your face.")
        print("Ending 7: You have been knocked out")
    else:
        print("Invalid Choice. Try Again\n")
        sunbathe()


def block():
    print("You put your hands up to block it.")
    block_chance = random.randint(1, 5)
    if block_chance == 2:
        print("You have blocked it!")
        print("1. Bring the ball inside")
        print("2. Throw it back over your fence")
        print("3. Just leave it and go back inside")
        
        choice = input("> ")
        if choice == "1":
            print("You pick up the ball and walk inside to put it away.")
            bedroom()
        elif choice == "2":
            print("The ball lands on the other side.")
            backyard()
        elif choice == "3":
            print("You leave the ball sitting on the grass.")
            backyard()
        else:
            print("Invalid Choice. Returning to backyard.\n")
            backyard()
    else:
        print("The ball hits your face.")
        print("Ending 6: You have been knocked out")


def shed_outside():
    print("As you get close to the shed you hear a noise.")
    print("1. Enter")
    print("2. Go Back")
    
    choice = input("> ")
    if choice == "1":
        shed_inside()
    elif choice == "2":
        backyard()
    else:
        print("Invalid Choice. Try Again\n")
        shed_outside()


def shed_inside():
    print("You open the shed and a raccoon jumps at you!")
    print("1. Shut the door")
    print("2. Run")
    
    choice = input("> ")
    if choice == "1":
        shut()
    elif choice == "2":
        run()
    else:
        print("Invalid Choice. Try Again\n")
        shed_inside()


def shut():
    print("As you try to shut the door...")
    shut_chance = random.randint(1, 10)
    if shut_chance == 2:
        print("You managed to shut the door just in time!")
        backyard()
    else:
        print("You couldn't shut it in time.")
        print("Ending 5: You Got Mauled by a raccoon")


def run():
    print("You decide to run inside.")
    print("You made it!")
    bedroom()


def swim():
    global showered
    print("You approach the edge of the pool.")
    print("1. Jump into the water")
    print("2. Take the stairs in the pool")
    print("3. Go back")
    
    choice = input("> ")
    if choice == "1":
        print("You jump into the water and then you get out.")
        showered = False
        swim()
    elif choice == "2":
        print("As you take the stairs you slip.")
        print("Ending 4: You hit your head")
    elif choice == "3":
        backyard()
    else:
        print("Invalid Choice. Try Again\n")
        swim()


def go_neighbors_pool():
    print("You sneak into your neighbor's yard.")
    print("They catch you and you go to prison for 12 years.")
    print("Ending 1: You got caught")


def kitchen():
    global hands_washed, dishes_done
    print("1. Open Fridge")
    print("2. Do the Dishes")
    print("3. Wash your Hands")
    
    choice = input("> ")
    if choice == "1":
        if hands_washed and dishes_done:
            open_fridge()
        else:
            print("Your chores are not done.")
            kitchen()
    elif choice == "2":
        do_dishes()
    elif choice == "3":
        wash_hands()
    else:
        print("Invalid Choice. Try Again\n")
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
        print("Invalid Choice. Try Again\n")
        bedroom()


def bathroom():
    print("1. Take a Shower")
    
    choice = input("> ")
    if choice == "1":
        shower()
    else:
        print("Invalid Choice. Try Again\n")
        bathroom()


def open_fridge():
    print("You have decided to open the fridge.")
    print("You have 2 cheeses, 2 types of sandwich meats, and 1 condiment.")
    print("1. Swiss, Ham, Mayo")
    print("2. Swiss, Turkey, Mayo")
    print("3. American, Ham, Mayo")
    print("4. American, Turkey, Mayo")
    print("5. Decide not to eat")
    
    choice = input("> ")
    if choice in ("1", "2", "3", "4"):
        print("Your sandwich looks absolutely perfect.")
        print("1. Eat it right now at the table")
        print("2. Take it outside to enjoy the sunshine")
        
        food_choice = input("> ")
        if food_choice == "1":
            print("Delicious! You happily finish your lunch and feel great.")
            print("Ending 9: A Well Fed Life")
        elif food_choice == "2":
            print("As soon as you walk outside, a stray dog sprints by and snatches it from your hands!")
            print("Ending 10: Robbed by a Good Boy")
        else:
            print("Invalid Choice. You dropped your sandwich in confusion.\n")
            enter_house()
    elif choice == "5":
        print("You have decided to starve.")
        print("Ending 3: You Have Starved")
    else:
        print("Invalid Choice. Try Again\n")
        open_fridge()


def sleep():
    print("You were too tired to make food.")
    print("Ending 2: Go to Sleep")


def shower():
    global showered
    print("You chose to shower. You feel clean now.")
    showered = True
    print("1. Leave Bathroom")
    
    choice = input("> ")
    if choice == "1":
        enter_house()
    else:
        print("Invalid Choice. Try Again\n")
        shower()


def make_bed():
    global wallet
    print("You look at your messy bed and decide to make it look nice.")
    cash_found = random.randint(1, 20)
    wallet += cash_found
    print("You found $",cash_found, "while making your bed.")
    print("You Have: $",wallet)
    print("1. Leave Bedroom")
    
    choice = input("> ")
    if choice == "1":
        enter_house()
    else:
        print("Invalid Choice. Try Again\n")
        make_bed()


def do_dishes():
    global dishes_done
    print("You look at the full sink and decide to do dishes.")
    dishes_done = True
    print("1. Leave Kitchen")
    print("2. Wash Hands")
    
    choice = input("> ")
    if choice == "1":
        enter_house()
    elif choice == "2":
        wash_hands()
    else:
        print("Invalid Choice. Try Again\n")
        do_dishes()


def wash_hands():
    global hands_washed
    print("You wash your hands.")
    hands_washed = True
    print("1. Leave Kitchen")
    
    choice = input("> ")
    if choice == "1":
        enter_house()
    else:
        print("Invalid Choice. Try Again\n")
        wash_hands()

start()
