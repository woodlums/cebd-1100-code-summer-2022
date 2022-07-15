# for x in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
#     print(x)

# for x in range(0, 10):
#
#     if x == 5:
#         break
#
#     print(x)

vowel_list = ["A", "E", "I", "O", "U"]
test_string = "Brendan"
vowel_count = 0
for a in test_string:
    a = a.upper()
    if a == "A" or a == "I" or a == "O" or a == "E" or a == "U":
    # if a in vowel_list:
        vowel_count += 1
print(vowel_count)




# print(list(range(0,10,2)))


