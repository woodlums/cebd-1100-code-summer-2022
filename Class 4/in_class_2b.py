# Draw a triangle according to user specified size.

size = input("Enter the size of the square: ")

size = int(size)

y = 1
x = 1

while y <= size:

    x = 0
    while x <= y:

        print("X", end="")
        x = x + 1

    y = y + 1
    print()
