# --- LOGISTICS INPUTS ---
traveler_name = input("Enter traveler name\n> ") #Get Traveler Name from User
destination = input("Enter destination\n> ") #Get Destination from User
dep_month = input("Enter departure month\n> ") #Get Departure Month from User
dep_day = int(input("Enter departure day\n> ")) #Get Departure Day from User
trip_length = int(input("Enter trip length in days\n> ")) #Get Trip Length from User

# --- ACCOMMODATIONS INPUTS ---
trans_type = input("Enter transportation type\n> ") #Get Transportation Type from User
ticket_price = float(input("Enter ticket price\n> ")) #Get Ticket Price from User
hotel_name = input("Enter hotel name\n> ") #Get Hotel Name from User
room_price = float(input("Enter nightly room price\n> ")) #Get Nightly Room Price from User
num_rooms = int(input("Enter number of rooms\n> ")) #Get Number of Rooms from User

# --- ACTIVITIES & BUDGET INPUTS ---
activity_1 = input("Enter planned activity 1\n> ") #Get Planned Activity 1 from User
activity_2 = input("Enter planned activity 2\n> ") #Get Planned Activity 2 from User
activity_3 = input("Enter planned activity 3\n> ") #Get Planned Activity 3 from User
spend_budget = float(input("Enter spending budget\n> ")) #Get Spending Budget from User
souvenir_budget = float(input("Enter souvenir budget\n> ")) #Get Souvenir Budget from User


def get_logistics_heading(): #Returns Travel Logistics Heading
    return "\n========== TRAVEL LOGISTICS =========="


def get_transit_heading(): #Returns Transit and Lodging Heading
    return "\n========== TRANSIT & LODGING =========="


def get_activities_heading(): #Returns Activities and Budget Heading
    return "\n========== ACTIVITIES & BUDGET =========="


def print_completed_report(): #Prints the Completed Report
    # Print Section 1: Travel Logistics
    print(get_logistics_heading())
    print("Traveler Name: ", traveler_name)
    print("Destination: ", destination)
    print("Departure Month: ", dep_month)
    print("Departure Day: ", dep_day)
    print("Trip Length in Days: ", trip_length)

    # Print Section 2: Transit and Lodging
    print(get_transit_heading())
    print("Transportation Type: ", trans_type)
    print("Ticket Price: ", ticket_price)
    print("Hotel Name: ", hotel_name)
    print("Nightly Room Price: ", room_price)
    print("Number of Rooms: ", num_rooms)

    # Print Section 3: Activities and Budget
    print(get_activities_heading())
    print("Activity 1: ", activity_1)
    print("Activity 2: ", activity_2)
    print("Activity 3: ", activity_3)
    print("Spending Budget: ", spend_budget)
    print("Souvenir Budget: ", souvenir_budget)


print_completed_report() #Print complete Travel Plan
