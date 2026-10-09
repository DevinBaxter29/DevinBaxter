
question_1 = input("What is the capital of France?\n> ")       #Get Answer 1
question_2 = input("How many sides does a square have?\n> ")   #Get Answer 2
question_3 = input("What color is the sky?\n> ")               #Get Answer 3
question_4 = input("What is the Color of the Sun?\n> ")  #Get Answer 4
question_5 = input("What is the largest ocean?\n> ")            #Get Answer 5

def tally_score(question_1, question_2, question_3, question_4, question_5):  #Tally Score
    score = 0

    if question_1 == "Paris":
        score = + 1

    if question_2 == "4":
        score = + 1

    if question_3 == "Blue":
        score = + 1

    if question_4 == "White":
        score = + 1

    if question_5 == "Pacific":
        score = + 1

    return score


score = tally_score(question_1, question_2, question_3, question_4, question_5)  #Get Score

print("Your Score Is: " + str(score) + "/5")  #Prints Final Score