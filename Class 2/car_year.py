purchase_year = input("When was the car purchased? >")
current_year = input("What is the current year? >")

purchase_year = int(purchase_year)
current_year = int(current_year)

years_old = current_year - purchase_year
months_old = years_old * 12
days_old = years_old * 365

print("Num years old = " + str(years_old))
print("Num months old = " + str(months_old))
print("Num days old = " + str(days_old))
