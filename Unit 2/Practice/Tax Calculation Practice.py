item_input = input("Enter the name of the item: ")
price_input = float(input("Enter the cost of the item in dollars: "))
tax_rate = 1.06875


def calculate_tax(item, price, rate):
 print(item + " costs " + str(price) + " dollars before tax and " + str(round(price_input * rate)) + " after tax.")

calculate_tax(item_input, price_input, tax_rate)
