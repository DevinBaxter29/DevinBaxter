wind = int(input("What is the wind speed?\n> "))

if wind < 74:
    print("Tropical Storm")
elif wind < 96:
    print("Category 1")
elif wind < 111:
    print("Category 2")
elif wind < 130:
    print("Category 3")
elif wind < 157:
    print("Category 4")
else:
    wind >= 157
    print("Category 5")