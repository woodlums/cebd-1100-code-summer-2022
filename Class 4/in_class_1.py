# Ask user for size of square
# Draw a square of that size.

# 3

# print("X", end="")
# print("X", end="")
# print("X")
# print("X", end="")
# print("X", end="")
# print("X")
# print("X", end="")
# print("X", end="")
# print("X")

# Use for loops to automate this.
# you will need 2 for loops.
# you need to convert what the user enters to an integer.

size = int(input("Enter the size of the square: "))

for y in range(size):

    for x in range(size):

        print("X", end="")

    print()


