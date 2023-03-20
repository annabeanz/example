# 1. Percentage change
"""
get input_value, percentage_rate
result = input_value * (1 + percentage_rate/100)
print original, change, result
"""
input_value = float(input("What is your value: "))
percentage_rate = float(input("Percentage rate it changed by: "))
result = input_value * (1 + percentage_rate/100)
print(f" Original: {input_value}, Change: {percentage_rate}, result {result}")

# 2. Time of day
"""
get time_of_day, coming_going
if time_of_day > 12
    display morning_message
else
    display noon_message
if coming_going == coming 
    display greeting
else 
    display parting
"""
time_of_day =  int(input("What time is it?: "))
coming_going = input("Are you coming or going?: ")
if time_of_day > 12:
    time_of_day = "before noon"
else:
    time_of_day = "after noon"
if coming_going == "coming":
    coming_going = "coming. Hi"
else:
    coming_going = "going. Bye!"
print(f"It is {time_of_day} and you are {coming_going}", sep="")

# 3. Coffee orders
"""
get coffee_type, size
if size == small
    cost = 3
else if size == medium
    cost = 4
else if size == large
    cost = 5
if coffee_type != black
    cost += 1
print order_message, cost
"""
coffee_type = input("Would you like black or white coffee?: ").lower()
size = input("What size?: ").lower()
if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if coffee_type != "black":
    cost += 1
print(f"Your total will be ${cost} for a {size} {coffee_type} coffee", sep="")
print("I hope you a good day! :)")

# 4.
"""
get coffee_type, size
while size != small or medium or large
    display error_message
    get size
if size == small
    cost = 3
else if size == medium
    cost = 4
else if size == large
    cost = 5
while coffee_type != white or black
    display error_message
    get coffee_type
if coffee_type != black
    cost += 1
print order_message, cost
"""
coffee_type = input("Would you like black or white coffee?: ").lower()
while coffee_type != "black" and coffee_type != "white":
    print("Please enter a valid input! we only have black or white coffee.")
    coffee_type = input("Would you like black or white coffee?: ").lower()

size = input("What size?: ").lower()
while size != "small" and size != "medium" and size != "large":
    print("Please enter a valid input! we only have small, medium or large.")
    size = input("What size?: ").lower()

if size == "small":
    cost = 3
elif size == "medium":
    cost = 4
else:
    cost = 5
if coffee_type != "black":
    cost += 1
print(f"Your total will be ${cost} for a {size} {coffee_type} coffee", sep="")
print("I hope you a good day! :)")

#5. Accumulation
"""
count = 0
get low_value, high_value
for number from low_value to high_value
    display number
    count += number
display count
"""
count = 0
low_value = int(input("Give a low value: "))
high_value = int(input("Give a high value: "))
while high_value < low_value:
    print(f"Please give a number HIGHER than the low value!")
    high_value = int(input("Give a high value: "))
for number in range(low_value, high_value+1):
    print(number, end=" ")
    count += number
print(f"will total to {count}")