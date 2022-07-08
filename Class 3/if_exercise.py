# diners = int(input("How many people are waiting? >"))
#
# print ("Your table is ", end="")
#
# if diners >= 8:
#     print("not ", end="")
#
# print("ready.")


num = int(input("Enter an integer greater than 0. >"))

if num > 0:
    if num % 10 == 0:
        print("Multiple of 10.")
    else:
        print("Not a multiple of 10")
else:
    print("Sorry the number must be greater than 0.")
