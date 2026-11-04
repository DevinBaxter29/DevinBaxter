countdown = (10,9,8,7,6,5,4,3,2,1)


for x in countdown:
    print(x)

for x in countdown:
    total_sum = sum(countdown)
print(total_sum)

list_one = (1,2,3,4,5)

for x in list_one:
    print(x**2)

string = input("Enter a String\n> ")

for x in string:
    count = 0
    vowels = "aeiouAEIOU"
    if x in vowels:
        count += 1
        print(count)

number = int(input("Enter a number\n> "))

for x in countdown:
    print(str(number) + " x " + str(x) + " = " + str(number * x))


names = ["Alice", "Bob", "Charlie"]

for x in names:
    print("Hello, " + x)