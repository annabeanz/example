# Example 01
"""get original_price and surcharge_rate
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
display total_price  """

original_price = float(input("Original price: $"))
surcharge_rate = float(input("Surcharge % (e.g. 0.15 is 15%): "))
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
print("The total meal price is $", total_price, sep="")

