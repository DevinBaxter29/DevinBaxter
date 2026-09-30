num_apples = float(input("How many apples do you have?\n> "))
num_people = int(input("How many people are there?\n> "))


def serve(people,apples_per_person):
    print("Served " + str(people), "people a glass of apple juice at ", str(apples_per_person), "Per glass.")

def portion(apples, people):
    return apples/people
    

ratio = portion(num_apples, num_people)

serve(num_people, ratio)