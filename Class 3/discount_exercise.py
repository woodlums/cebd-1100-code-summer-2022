import random

type_code = "R"
invoice_total = random.randint(0, 1000)
discount = 0.0

print(invoice_total)

# if type_code == "R" and invoice_total >= 100 and invoice_total < 250:
#     discount = .1
# elif type_code == "R" and invoice_total >= 250:
#     discount = .2
# elif type_code == "W" and invoice_total < 500:
#     discount = .4
# elif type_code == "W" and invoice_total >= 500:
#     discount = .5

if type_code == "R":
    if invoice_total >= 100 and invoice_total < 250:
        discount = .1
    elif invoice_total >= 250:
        discount = .2
    # extra logic here....

if type_code == "W":
    if invoice_total < 500:
        discount = .4
    else:
        discount = .5


print(discount)
