countdown = [1,2,3,4,5,6,7,8,9,10]


for x in countdown:
    print(x)

sum = 0
for x in countdown:
    sum = sum + x
print(sum)

list_one = [1,2,3,4,5]

for x in list_one:
    print(x**2)

string = input("Enter a String\n> ")

for x in string:
    count = 0
    vowels = "aeiouAEIOU"
    if x in string:
        count += 1
print(count)

number = int(input("Enter a number\n> "))

for x in countdown:
    print(str(number) + " * " + str(x) + " = " + str(number * x))


names = ["Alice", "Bob", "Charlie","Mark","Alexa"]

for x in names:
    print("Hello, " + x)