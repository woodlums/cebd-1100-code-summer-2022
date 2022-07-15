answer_list = ['Y', 'y', 'yep']

x = "Y"

#while x == "Y" or x == "Yes" or x == "A":

while x in answer_list:
    print("OK continuing")
    x = input("Continue again? >")
