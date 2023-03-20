# 1. Discount Price
"""
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""
DISCOUNT_RATE = 0.2
original_price = float(input("What is the original price?:"))
discount = original_price * DISCOUNT_RATE
discounted_price = original_price - discount
print(discounted_price)

# 2. Kilometres to Miles
"""
kilometer_to_mile_constant = 0.6213712
get number_of_kilometers 
number_of_miles = number_of_kilometers * kilometer_to_mile_constant
print number_of_miles
"""
KILOMETER_TO_MILE_COEFFICIENT = 0.6213712
number_of_kilometres = int(input("Kilometres: "))
number_of_miles = number_of_kilometres * KILOMETER_TO_MILE_COEFFICIENT
print(number_of_miles)

# 3. Holiday Cost
"""
get food_cost, hotel_cost, activity_cost, number_of_days
total_cost = sum(food_cost, hotel_cost, activity_cost, number_of_days) * number_of_days
print total_cost
"""
daily_hotel_cost = float(input("How much does the hotel cost?: $"))
daily_food_cost = float(input("How much do you spend on food daily?: $"))
daily_activity_cost = float(input("How much do you spend on activities daily?: $"))
number_of_days = int(input("How many days are you staying?:"))
total_cost = daily_activity_cost + daily_food_cost + daily_hotel_cost * number_of_days
print ("Your total is: $", total_cost,sep="")

# 4. Deep Sleep Calculation (Percentage)
"""
get total_sleep_in_seconds, deep_sleep_in_seconds
percentage_deepsleep = total_sleep_in_seconds / deep_sleep_in_seconds
"""
total_sleep_in_seconds = float(input("Total seconds slept:"))
total_deep_sleep_in_seconds = float(input("Deep sleep seconds slept:"))
percentage_deep_sleep = (total_deep_sleep_in_seconds / total_sleep_in_seconds) * 100
deep_sleep_min = int(total_deep_sleep_in_seconds // 60)
deep_sleep_sec = int(total_deep_sleep_in_seconds % 60)
sleep_min =int(total_sleep_in_seconds//60)
sleep_sec = int(total_sleep_in_seconds % 60)
print("Total sleep time:", sleep_min, "min and",sleep_sec, "sec")
print ("Deep sleep time:", deep_sleep_min, "min and", deep_sleep_sec, "sec")
print ("Percentage deep sleep:", percentage_deep_sleep,"%", sep="")