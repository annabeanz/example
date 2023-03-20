# 1. Tax
"""
get taxable_amount
TAX BRACKET 1 = 0.00
TAX_BRACKET_2 = 0.05
TAX BRACKET 3 = 0.10
if taxable_amount < 100
    print taxable_amount * TAX_BRACKET_1
else if taxable_amount < 1000
    print taxable_amount * TAX_BRACKET_2
else if taxable_amount >= 1000
    print taxable_amount * TAX_BRACKET_3
"""


taxable_amount = float(input("What is your monly income in USD?:"))
TAX_BRACKET_1 = 0.00
TAX_BRACKET_1B = 0.02
TAX_BRACKET_2 = 0.05
TAX_BRACKET_3 = 0.10
if taxable_amount < 100:
    tax = taxable_amount * TAX_BRACKET_1
elif taxable_amount < 500:
    tax = taxable_amount * TAX_BRACKET_1B
elif taxable_amount < 1000:
    tax = taxable_amount * TAX_BRACKET_2
elif taxable_amount >= 1000:
    tax = taxable_amount * TAX_BRACKET_2
print("Your tax payment is: $", tax)
print("Your take home pay is: $", taxable_amount)

#2. Car Insurance
"""
get age 
if age < 18 
    print "Hire refused"
else if age < 25 
    print "Insurance required"
else print "Insurance not required"
"""

age = int(input("""Welcome to Painz car insurance!!
What is your age?:"""))
if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else: print("Insurance not required")

#3. Simple Password Checker
"""
PASSWORD = Incorrect101
get password_input
if password_input == PASSWORD
    print "access granted"
else: print "Access denied"
"""

PASSWORD = "Incorrect101"
password_input = input("Please enter your secret password:")
if password_input == PASSWORD:
    print("Access granted")
else: print("Access denied")

#4. Dog years
"""
get age 
if age <= 2
    dog_years = age * 10.5
elif age > 2
    dog_years = ((age - 2) * 10.5 + age * 4
print "Your age in dog years is:" dog_years
"""

age = int(input("""Do you want to know your age in dog years?
Tell me your age:"""))
if age <= 2:
    dog_years = age * 10.5
elif age > 2:
    dog_years = ((age - 2) * 10.5 + age * 4)
print("Your age in dog years is:",dog_years)

#5. Rock of Ages
"""
get age 
if age == 18 
    print "YOOO YOU ARE THE SAME AGE AS ME!! whoop whoop"
else if age < 8
    print "what are you doing here child?"
else if age < 18
    print "haha you child you are younger than me"
else if age > 20 
    print "you are older than me.... oh..."
"""
age = int(input("what is your age?:"))
if age == 18:
    print("YOOO YOU ARE THE SAME AGE AS ME!! whoop whoop")
elif age < 8:
    print("what are you doing here child?")
elif age < 18:
    print("haha you child you are younger than me")
elif age > 20:
    print("you are older than me.... oh...")

# 6. Speeding Fines
"""
get speed_limit, speed
speed_over = speed - speed_limit
if speed_over < 0
    print("you are not overthe limit")
else if speed_over < 13
    infringement = 177
else if speed_over < 20
    infringement = 266
else if speed_over < 30
    infringement = 444
else if speed_over < 40
    infringement = 622
else if speed_over < 40
    infringement = 1245
"""
speed_limit = int(input("What was the speed limit?"))
speed = float(input("What speed were you going at?"))
speed_over = speed - speed_limit
if speed_over < 0:
    infringement = 0
    print("you are not over the limit")
elif speed_over < 13:
    infringement = 177
elif speed_over < 20:
    infringement = 266
elif speed_over < 30:
    infringement = 444
elif speed_over < 40:
    infringement = 622
elif speed_over < 40:
    infringement = 1245
print("Your infringement cost you $",infringement)
