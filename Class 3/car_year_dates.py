import datetime
from dateutil import relativedelta

car_purchase_date = datetime.datetime(2018, 1, 1)
current_date = datetime.datetime.now()

print(car_purchase_date.strftime("%Y-%m-%d"))

delta = relativedelta.relativedelta(current_date, car_purchase_date)

print(delta.years)
print(delta.months)
print(delta.days)

total_months = (delta.years * 12) + delta.months
print("Total months since the car purchase is " + str(total_months))


# Display the date formatted - strftime



