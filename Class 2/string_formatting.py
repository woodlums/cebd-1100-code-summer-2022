first = "Brendan"
last = "Wood"
age = 35

greeting0 = "Hello, " + first + " " + last + " you are " + str(age) + " years old."

greeting1 = "Hello, {1} {0} you are {2} years old".format(first, last, age)

greeting1b = "Hello, {firstname} {lastname} you are {personage} years old" \
    .format(firstname = first, lastname = last, personage = age)

greeting2 = f"Hello, {first} {last} you are {age} years old"

print(greeting1)

print("{:04d}".format(42))

print('{:d}'.format(42))
print('{:f}'.format(42))
print('{:s}'.format("42"))
print('{:%}'.format(0.42))

print("You owe ${:.2f}".format(12))


