
x_value = int(input("Enter Number\n>"))  #Get X value from User
y_value = int(input("Enter Number\n>"))  #Get Y value from User

def add(x, y):           #Adds 2 Integers
    return x + y

def subtract(x,y):       #Subtracts 2 Integers
    return x - y

def multiply(x,y):       #Multiplies 2 Integers
    return x * y

def divide(x,y):         #Divides 2 Integers
    return x / y

def exponent(x,y):       #Uses Y as an Exponent
    return x ** y

def modulus(x,y):        
    return x % y

def floor_division(x,y): #Uses Floor Division
    return x // y


#Prints the result of all Actions

print("Addition Result: ", add(x_value, y_value))
print("Subtraction Result: ", subtract(x_value, y_value))
print("Multiplication Result: ", multiply(x_value, y_value) )
print("Division Result: ", divide(x_value, y_value))
print("Exponent Result: ", exponent(x_value, y_value))
print("Modulus Result: ", modulus(x_value, y_value))
print("Floor Division Result: ", floor_division(x_value, y_value))
