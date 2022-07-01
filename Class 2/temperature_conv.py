temp = int(input("What is the temperature value to convert? >"))


f_value = 9 / 5 * temp + 32

# Formula for converting to Celcius.
c_value = (temp - 32) / (9 / 5)

# Print temp in F
print("Temperature in F")
print(round(f_value, 2))

# Print temp in C
print("Temerature in C")
print(round(c_value, 2))
