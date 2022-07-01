from decimal import Decimal

FEDERAL_TAX = Decimal("0.05")
PROVINCIAL_TAX = Decimal("0.09775")
meal_price = Decimal("44.99")
meal2_price = Decimal("109.99")

# Do calculations for tax.
price_including_tax = (meal_price * FEDERAL_TAX) + (meal_price * PROVINCIAL_TAX) + meal_price
price_including_tax2 = (meal2_price * FEDERAL_TAX) + (meal2_price * PROVINCIAL_TAX) + meal2_price

# Print the results of the taxes.
print(price_including_tax)  # Display result
print(price_including_tax2)


# CTRL+/