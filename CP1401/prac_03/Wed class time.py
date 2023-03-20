size_of_land = float(input("what is the zie of the land in sq meters?:"))
price_per_sq_meter = float(input("what is the price per sq meter?: $"))
price_of_house_land = float(input("what is the price of the house itself?: $"))
price_of_the_house = (size_of_land * price_per_sq_meter) + price_of_house_land
print ("the price of the house is: $%.2f" %price_of_the_house)

""" 
get age 
if age >= 18:
    allow
else: deny
"""
age = int(input("what is your age?:"))
if age >= 18:
    print("allow")
else: print("entry denied")

greeting = input("hi?:")
if greeting == "h":
    print ("hello")
else: print ("whatever")

score = float(input(":"))
if score >= 50:
    print("yes")
if score >= 60:
    print("yes yes")
else: print("no no")
if score >= 55:
    print("yes yes yes")

False
True
False

#NOT>AND>OR