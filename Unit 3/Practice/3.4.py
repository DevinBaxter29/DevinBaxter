def mult():
    num_one = input("Give a number\n> ")
    num_two = input("Give a number\n> ")
    try:
        print(float(num_one) * float(num_two))
    except:
        print("INVALID INPUT. TRY AGAIN\n> ")
        mult()

mult()