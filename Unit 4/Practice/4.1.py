fruit_list = ["apples","banana","mango","watermelon","orange"]

print(fruit_list[0])
print(fruit_list[-1])


new_fruit = input("What fruit should be added\n> ")
fruit_list.append(new_fruit)

print(fruit_list)


removed_fruit = input("What fruit should go\n> ")
fruit_list.remove(removed_fruit)

fruit_list.sort()

print(fruit_list)



for fruit in fruit_list:
    print(fruit)