#Calculating BMI
"""
get height
get weight
bmi = weight / (height ** 2)
display bmi
"""
height_m = float(input("What is your height in m?: "))
weight_kg = float(input("what is your weight in kg?: "))
bmi = weight_kg / (height_m ** 2)
print ("Your bmi is:", bmi)


# Decimal places
"""
get bmi (from previous question)
print bmi with 2dp
"""
print ("Your BMI is:%.2f" % bmi )

#Converter
"""
get fahrenheit , inches, pounds, SGD
celsius = fahrenheit  
centimeters = inches 
kilograms = pounds
USD = SGD
"""
celsius = float(input("fahrenheit: ")) - 17.22
centimeters = float(input("inches: ")) * 0.3937008
kilograms = float(input("pounds: ")) * 2.204623
usd = float(input("SGD: ")) * 1.37
print("""
celsius = %.2f
centimeters = %.2f
kilograms = %.2s
USD = %.2s""" % (celsius,centimeters,kilograms,usd))




