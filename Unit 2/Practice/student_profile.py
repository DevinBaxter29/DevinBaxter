#1
name = input("Enter student name\n> ") #Get Name from User
age = int(input("Enter student age\n> ")) #Get Age from User
hometown = input("Enter hometown\n> ") #Get Hometown from User
fav_food = input("Enter favorite food\n> ") #Get Favorite Food from User
fav_hobby = input("Enter favorite hobby\n> ") #Get Favorite Hobby from User
#2
school_name = input("Enter school name\n> ") #Get School Name from User
grade_level = input("Enter grade level\n> ") #Get Grade Level from User
fav_subject = input("Enter favorite subject\n> ") #Get Favorite Subject from User
study_hours = float(input("Enter study hours per week\n> ")) #Get Study Hours from User
grad_year = int(input("Enter graduation year\n> ")) #Get Graduation Year from User
#3
dream_job = input("Enter dream job\n> ") #Get Dream Job from User
skill_to_learn = input("Enter skill to learn\n> ") #Get Skill to Learn from User
place_to_visit = input("Enter place to visit\n> ") #Get Place to Visit from User
personal_goal = input("Enter personal goal\n> ") #Get Personal Goal from User
school_goal = input("Enter school goal\n> ") #Get School Goal from User

def get_personal_heading(): #Returns Personal Details Heading
    return "\n========== PERSONAL PROFILE =========="


def get_academic_heading(): #Returns Academic Details Heading
    return "\n========== ACADEMIC PROFILE =========="


def get_goals_heading(): #Returns Future and Goals Heading
    return "\n========== FUTURE & GOALS =========="
#Prints Completed Report
def completed_report():
    #Prints Personal Report
    print(get_personal_heading())
    print("Name: ", name)
    print("Age: ", age)
    print("Hometown: ", hometown)
    print("Favorite Food: ", fav_food)
    print("Favorite Hobby ", fav_hobby)

    #Prints School Report
    print(get_academic_heading())
    print("School: ", school_name)
    print("Grade: ", grade_level)
    print("Favorite Subject: ", fav_subject)
    print("Study Hours: ", study_hours)
    print("Graduation Year: ", grad_year)

    #Prints Goal Report
    print(get_goals_heading())
    print("Dream Job: ", dream_job)
    print("Skill to Learn: ", skill_to_learn)
    print("Place to Visit: ", place_to_visit)
    print("Personal Goal: ", personal_goal)
    print("School Goal: ", school_goal)


completed_report()

