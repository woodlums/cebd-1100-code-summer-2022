# Draw a triangle according to user specified size.

size = int(input("Enter the size of the square: "))

for y in range(1, size + 1):

    for x in range(y):

        print("X", end="")

    print()
