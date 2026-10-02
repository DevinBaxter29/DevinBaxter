p1_name = input("Enter product 1 name\n> ") #Get Product 1 Name from User
p1_desc = input("Enter product 1 description\n> ") #Get Product 1 Description from User
p1_price = float(input("Enter product 1 price\n> ")) #Get Product 1 Price from User
p1_qty = int(input("Enter product 1 quantity in stock\n> ")) #Get Product 1 Quantity from User
p1_weight = float(input("Enter product 1 weight\n> ")) #Get Product 1 Weight from User

p2_name = input("Enter product 2 name\n> ") #Get Product 2 Name from User
p2_desc = input("Enter product 2 description\n> ") #Get Product 2 Description from User
p2_price = float(input("Enter product 2 price\n> ")) #Get Product 2 Price from User
p2_qty = int(input("Enter product 2 quantity in stock\n> ")) #Get Product 2 Quantity from User
p2_weight = float(input("Enter product 2 weight\n> ")) #Get Product 2 Weight from User

p3_name = input("Enter product 3 name\n> ") #Get Product 3 Name from User
p3_desc = input("Enter product 3 description\n> ") #Get Product 3 Description from User
p3_price = float(input("Enter product 3 price\n> ")) #Get Product 3 Price from User
p3_qty = int(input("Enter product 3 quantity in stock\n> ")) #Get Product 3 Quantity from User
p3_weight = float(input("Enter product 3 weight\n> ")) #Get Product 3 Weight from User


def get_p1_heading(): #Returns Product 1 Heading
    return "\n========== PRODUCT 1 DETAILS =========="


def get_p2_heading(): #Returns Product 2 Heading
    return "\n========== PRODUCT 2 DETAILS =========="


def get_p3_heading(): #Returns Product 3 Heading
    return "\n========== PRODUCT 3 DETAILS =========="


def print_completed_report(): #Prints the Completed Report
    # Print Product 1 Section
    print(get_p1_heading())
    print("Product Name: ", p1_name)
    print("Description: ", p1_desc)
    print("Price: ", p1_price)
    print("Quantity in Stock: ", p1_qty)
    print("Weight: ", p1_weight)

    # Print Product 2 Section
    print(get_p2_heading())
    print("Product Name: ", p2_name)
    print("Description: ", p2_desc)
    print("Price: ", p2_price)
    print("Quantity in Stock: ", p2_qty)
    print("Weight: ", p2_weight)

    # Print Product 3 Section
    print(get_p3_heading())
    print("Product Name: ", p3_name)
    print("Description: ", p3_desc)
    print("Price: ", p3_price)
    print("Quantity in Stock: ", p3_qty)
    print("Weight: ", p3_weight)


print_completed_report() #Print complete Product Catalog
