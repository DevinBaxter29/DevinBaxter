
import random

wallet = 0
dishes_done = False
hands_washed = False
showered = False
returned_wallet = False
job_posting_seen = False


def menu(*options):
    for option in options:
        print(option)
    return input("> ")


def play_again():
    print("Do you want to play again?")
    choice = menu('1. Yes', '2. No')

    if choice == "1":
        start()
    elif choice == "2":
        print("Thanks for playing Life!")
    else:
        print("Invalid choice. Try again.")
        play_again()


def start():
    print("Welcome to Life")
    print("You stand at the entrance of your home. Do you:")
    choice = menu('1. Enter your house', "2. Go to neighbor's yard", '3. Go to your backyard', '4. Visit the grocery store', '5. Walk around the neighborhood')
    if choice == "1":
        enter_house()
    elif choice == "2":
        go_neighbors_yard()
    elif choice == "3":
        backyard()
    elif choice == "4":
        grocery_store()
    elif choice == "5":
        lost_wallet()
    else:
        print("Invalid choice. Try again.\n")
        start()


def enter_house():
    print("You decide to enter your home.")
    print("You stand right inside your house. As you put your hat and jacket away you start to get hungry.")
    choice = menu('1. Go to Kitchen', '2. Go to Bedroom', '3. Go to Bathroom')
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
    choice = menu('1. Go Swimming', '2. Sunbathe', '3. Enter Shed', '4. Go Back')
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
    choice = menu('1. Try to block it', '2. Catch it', "3. Don't React")
    if choice == "1":
        block()
    elif choice == "2":
        print("You extend your hands to catch the ball...")
        catch_chance = random.randint(1, 5)
        if catch_chance == 2:
            print("You caught it right out of the air.")
            choice = menu('1. Bring the ball inside', '2. Throw it back over your fence', '3. Just leave it')
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
            play_again()
    elif choice == "3":
        print("You just sit there and stare.")
        print("The ball hits your face.")
        print("Ending 7: You have been knocked out")
        play_again()
    else:
        print("Invalid Choice. Try Again\n")
        sunbathe()


def block():
    print("You put your hands up to block it.")
    block_chance = random.randint(1, 5)
    if block_chance == 2:
        print("You have blocked it!")
        choice = menu('1. Bring the ball inside', '2. Throw it back over your fence', '3. Just leave it and go back inside')
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
        play_again()


def shed_outside():
    print("As you get close to the shed you hear a noise.")
    choice = menu('1. Enter', '2. Go Back')
    if choice == "1":
        shed_inside()
    elif choice == "2":
        backyard()
    else:
        print("Invalid Choice. Try Again\n")
        shed_outside()


def shed_inside():
    print("You open the shed and a raccoon jumps at you!")
    choice = menu('1. Shut the door', '2. Run')
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
        play_again()


def run():
    print("You decide to run away from the raccoon!")
    print("You sprint out of the shed and into the backyard.")
    print("The raccoon is still chasing you!")
    choice = menu('1. Run inside your house', '2. Climb over the fence', '3. Hide behind a tree')

    if choice == "1":
        print("You dash inside and slam the door shut.")
        print("You escape the raccoon safely!")
        bedroom()

    elif choice == "2":
        print("You try to climb over the fence.")
        fence_chance = random.randint(1, 3)

        if fence_chance == 1:
            print("You lose your grip and fall!")
            print("Ending 11: The Great Fence Fail")
            play_again()
        else:
            print("You make it over the fence and escape!")
            start()

    elif choice == "3":
        print("You hide behind a tree and hold your breath.")
        hide_chance = random.randint(1, 3)

        if hide_chance == 1:
            print("The raccoon finds you!")
            print("Ending 12: Found by the Furry Menace")
            play_again()
        else:
            print("The raccoon runs past without noticing you.")
            print("You quietly make your way back inside.")
            enter_house()

    else:
        print("Invalid choice. Try again.")
        run()


def swim():
    global showered

    print("You approach the edge of the pool.")
    print("The water looks refreshing.")
    choice = menu('1. Jump into the water', '2. Carefully take the pool stairs', '3. Sit by the pool', '4. Go back to the backyard')

    if choice == "1":
        print("You jump into the pool and enjoy the cool water!")
        showered = False

        print("You climb out of the pool, dripping wet.")
        choice = menu('1. Go inside and take a shower', '2. Dry off in the sun', '3. Go back into the pool')

        if choice == "1":
            print("You head inside to get cleaned up.")
            enter_house()
        elif choice == "2":
            print("You lie in the sun until you dry off.")
            backyard()
        elif choice == "3":
            print("You jump back into the pool.")
            swim()
        else:
            print("Invalid choice. Try again.")
            swim()

    elif choice == "2":
        print("You carefully descend the pool stairs.")
        print("You reach the water safely.")
        choice = menu('1. Swim around', '2. Get out of the pool')

        if choice == "1":
            print("You swim around and have a great time!")
            showered = False
            print("You climb out of the pool.")
            enter_house()
        elif choice == "2":
            print("You decide the water is too cold.")
            backyard()
        else:
            print("Invalid choice. Try again.")
            swim()

    elif choice == "3":
        print("You sit beside the pool and dip your feet in.")
        choice = menu('1. Relax a little longer', '2. Get up and go back')

        if choice == "1":
            print("You relax by the pool and enjoy the sunshine.")
            backyard()
        elif choice == "2":
            backyard()
        else:
            print("Invalid choice. Try again.")
            swim()

    elif choice == "4":
        backyard()

    else:
        print("Invalid choice. Try again.")
        swim()


def go_neighbors_yard():
    print("You sneak into your neighbor's yard.")
    print("As you enter, you see your neighbor watering their plants.")
    choice = menu('1. Sneak past the neighbor', '2. Talk to the neighbor', '3. Go back to your house')

    if choice == "1":
        print("You try to sneak past the neighbor.")
        sneak_chance = random.randint(1, 3)

        if sneak_chance == 1:
            print("The neighbor spots you!")
            choice = menu('1. Apologize', '2. Run away')

            if choice == "1":
                print("You apologize for entering their yard.")
                print("The neighbor accepts your apology.")
                start()
            elif choice == "2":
                print("You run away before the neighbor can stop you.")
                start()
            else:
                print("Invalid choice. Try again.")
                go_neighbors_yard()

        else:
            print("You sneak past the neighbor successfully!")
            print("You arrive at the swimming pool.")
            choice = menu('1. Go swimming', '2. Sneak back home')

            if choice == "1":
                swim()
            elif choice == "2":
                start()
            else:
                print("Invalid choice. Try again.")
                go_neighbors_yard()

    elif choice == "2":
        print("You walk over and greet your neighbor.")
        choice = menu('1. Ask if you can use the pool', '2. Say goodbye and leave')

        if choice == "1":
            print("Your neighbor agrees to let you use the pool!")
            swim()
        elif choice == "2":
            print("You say goodbye and return home.")
            start()
        else:
            print("Invalid choice. Try again.")
            go_neighbors_yard()

    elif choice == "3":
        print("You return safely to your house.")
        start()

    else:
        print("Invalid choice. Try again.")
        go_neighbors_yard()


def kitchen():
    global hands_washed, dishes_done
    choice = menu('1. Open Fridge', '2. Do the Dishes', '3. Wash your Hands')
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
    choice = menu('1. Make Bed', '2. Go to Sleep')
    if choice == "1":
        make_bed()
    elif choice == "2":
        sleep()
    else:
        print("Invalid Choice. Try Again\n")
        bedroom()


def bathroom():
    print("You enter the bathroom.")
    choice = menu('1. Take a Shower', '2. Brush Your Teeth', '3. Look in the Medicine Cabinet', '4. Return to the House')

    if choice == "1":
        shower()

    elif choice == "2":
        print("You pick up your toothbrush.")
        choice = menu('1. Brush your teeth', '2. Skip it and leave')

        if choice == "1":
            print("You brush your teeth until they feel clean.")
            print("You feel refreshed!")
            enter_house()
        elif choice == "2":
            print("You decide to skip brushing your teeth.")
            enter_house()
        else:
            print("Invalid choice. Try again.")
            bathroom()

    elif choice == "3":
        print("You open the medicine cabinet.")
        print("Inside, you find a bandage and a bottle of vitamins.")
        choice = menu('1. Take a bandage', '2. Take vitamins', '3. Close the cabinet')

        if choice == "1":
            print("You put the bandage in your pocket.")
            print("It might come in handy later.")
            enter_house()
        elif choice == "2":
            print("You take the vitamins and feel ready for the day.")
            enter_house()
        elif choice == "3":
            print("You close the cabinet and leave.")
            enter_house()
        else:
            print("Invalid choice. Try again.")
            bathroom()

    elif choice == "4":
        enter_house()

    else:
        print("Invalid choice. Try again.")
        bathroom()


def open_fridge():
    print("You have decided to open the fridge.")
    print("You have 2 cheeses, 2 types of sandwich meats, and 1 condiment.")
    choice = menu('1. Swiss, Ham, Mayo', '2. Swiss, Turkey, Mayo', '3. American, Ham, Mayo', '4. American, Turkey, Mayo', '5. Decide not to eat')
    if choice in ("1", "2", "3", "4"):
        print("Your sandwich looks absolutely perfect.")
        food_choice = menu('1. Eat it right now at the table', '2. Take it outside to enjoy the sunshine')
        if food_choice == "1":
            print("Delicious! You happily finish your lunch and feel great.")
            print("Ending 9: A Well Fed Life")
            play_again()
        elif food_choice == "2":
            print("As soon as you walk outside, a stray dog sprints by and snatches it from your hands!")
            print("Ending 10: Robbed by a Good Boy")
            play_again()
        else:
            print("Invalid Choice. You dropped your sandwich in confusion.\n")
            enter_house()
    elif choice == "5":
        print("You have decided to starve.")
        print("Ending 3: You Have Starved")
        play_again()
    else:
        print("Invalid Choice. Try Again\n")
        open_fridge()


def sleep():
    print("You enter your bedroom and feel extremely tired.")
    print("You lie down on your bed, but you aren't sure if you should sleep yet.")
    choice = menu('1. Go to sleep immediately', '2. Get a snack first', '3. Set an alarm and then sleep', '4. Get back up and make your bed')

    if choice == "1":
        print("You were too tired to do anything else.")
        print("Ending 2: Go to Sleep")
        play_again()

    elif choice == "2":
        print("You decide that you need something to eat.")
        kitchen()

    elif choice == "3":
        print("You set your alarm for tomorrow morning.")
        print("You get comfortable and fall asleep peacefully.")
        print("Ending 13: A Peaceful Night")
        play_again()

    elif choice == "4":
        print("You decide to be productive instead of sleeping.")
        make_bed()

    else:
        print("Invalid choice. Try again.")
        sleep()


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
    print("You found $", cash_found, "while making your bed.")
    print("You Have: $", wallet)
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
    choice = menu('1. Leave Kitchen', '2. Wash Hands')
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




def grocery_store():
    global wallet, job_posting_seen

    print("\nYou walk to the grocery store.")
    if job_posting_seen:
        print("You recognize the job flyer you saw earlier.")
    print("You have $", wallet, "in your wallet.")
    snack_price = 3 if returned_wallet else 5
    if returned_wallet:
        print("The store clerk heard you returned a lost wallet and offers you a discount.")
    print("What would you like to do?")
    print("1. Buy a snack for $",snack_price)
    choice = menu('2. Save your money and go home', '3. Look at the job board')

    if choice == "1":
        if wallet >= snack_price:
            wallet -= snack_price
            print("You buy a snack and enjoy it on the way home.")
            print("Money remaining: $", wallet)
            start()
        else:
            print("You don't have enough money for the snack.")
            print("You decide to head home and save up.")
            start()
    elif choice == "2":
        print("You decide to keep your money and head home.")
        start()
    elif choice == "3":
        job_posting_seen = True
        print("You see a flyer advertising a part-time job.")
        print("You remember the information in case you want to look for work later.")
        start()
    else:
        print("Invalid choice. Try again.\n")
        grocery_store()


def lost_wallet():
    global wallet, returned_wallet

    print("\nWhile walking around the neighborhood, you notice a wallet on the sidewalk.")
    print("What do you do?")
    choice = menu('1. Return it to its owner', '2. Look inside for identification', '3. Leave it where you found it')

    if choice == "1":
        print("You find the owner's address on a card and return the wallet.")
        print("The grateful owner gives you $10 as a thank-you.")
        wallet += 10
        returned_wallet = True
        print("You now have $", wallet)
        start()
    elif choice == "2":
        print("You find an ID card with the owner's name and address.")
        follow_up = menu('1. Take the wallet to the owner', '2. Leave the wallet where you found it')

        if follow_up == "1":
            print("You return the wallet to its owner.")
            print("The grateful owner gives you $10 as a thank-you.")
            wallet += 10
            returned_wallet = True
            print("You now have $", wallet)
            start()
        elif follow_up == "2":
            print("You put the wallet back and continue your walk.")
            start()
        else:
            print("Invalid choice. Try again.\n")
            lost_wallet()
    elif choice == "3":
        print("You leave the wallet where it is and head home.")
        start()
    else:
        print("Invalid choice. Try again.\n")
        lost_wallet()



start()
