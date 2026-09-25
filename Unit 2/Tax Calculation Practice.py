item_input = input("Enter the name of the item: ")
price_input = float(input("Enter the cost of the item in dollars: "))
rate_input = float(input("Enter the tax rate (6.875 for Minnesota): "))

def calculate_tax(item, price, rate):
 tax_amount = price * (rate / 100)
 total_price = price + tax_amount
 print(item + " costs " + (price) + " dollars before tax and " + (total_price) + " after tax.")

calculate_tax(item_input, price_input, rate_input)
