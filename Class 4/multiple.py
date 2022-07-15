CHECK_MULTIPLE = 15

while True:

    val = input("What is your test value? (Enter Q to quit) >")

    # Check if user entered "Q" and quit if necessary.
    #if val == "Q" or val == "q":
    if val.upper() == "Q":
        break

    val = int(val)

    if val % CHECK_MULTIPLE == 0:

        print("Yes the value is a multiple of " + str(CHECK_MULTIPLE) + ".")

    else:

        print(f"No the value is not a multiple of {CHECK_MULTIPLE}.")

print("Quitting program - Thanks for using the program.")



