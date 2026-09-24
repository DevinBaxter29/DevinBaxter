# One time, in a [adjective_1] [noun_1],
# there was a [adjective_2] [noun_2].
# Every night, the [noun_3] would [verb_1] [adverb_1].
# One morning, a [adjective_3] [noun_4] appeared
# and [verb_2] the [noun_5] away.

adjective_1 = input("Enter an adjective: ")  #Get adjective from User
adjective_2 = input("Enter an adjective: ")  #Get adjective from User
adjective_3 = input("Enter an adjective: ")  #Get adjective from User

noun_1 = input("Enter a noun: ")     #Get noun from User
noun_2 = input("Enter a noun: ")     #Get noun from User
noun_3 = input("Enter a noun: ")     #Get noun from User
noun_4 = input("Enter a noun: ")     #Get noun from User
noun_5 = input("Enter a noun: ")     #Get noun from User

verb_1 = input("Enter a verb: ")     #Get Verb from User
verb_2 = input("Enter a verb: ")     #Get Verb from User

adverb_1 = input("Enter an adverb: ") #Get adverb from User

print("One time, in a " + adjective_1, noun_1, "there was a " + adjective_2, noun_2, "Every night, the " + noun_3, "would ", verb_1, adverb_1,  "One morning, a " + adjective_3, noun_4, "appeared and " + verb_2, "the ", noun_5, "away." )  #Print complete Mad Lib 