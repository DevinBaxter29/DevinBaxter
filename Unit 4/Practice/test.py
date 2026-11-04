string = input("Enter a String\n> ")

for x in string:
    count = 0
    vowels = "aeiouAEIOU"
    if x in string:
        count += 1
print(count)