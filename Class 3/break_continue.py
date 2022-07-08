# i = 1
# while i < 6:
#         print(i)
#
#         if i == 3:
#             break
#
#         i += 1

# i = 0
# while i < 6:
#
#     i += 1
#
#     if i == 3:
#         continue
#
#     print(i)
#
# # 1 2 4 5


x = 0
y = 0

while x < 4:

    while y < 4:
        prod = x * y
        print(f"{x} times {y} is {prod}")
        y += 1
        continue

    y = 0
    x += 1
