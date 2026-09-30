
band = input("What band are you going to?\n> ")
num_people = int(input("How many people are going?\n> "))
ticket_price = int(input("Whats the price of a ticket?\n> "))

def show_cost(band,num_people,ticket_price):
    print("The cost for " + str(num_people), "people to go to", band, "is", (ticket_price * num_people),"." )

show_cost(band,num_people,ticket_price)