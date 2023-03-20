"""
function main()
    height = validate_input("height", 0, 3)
    weight = validate_input("Weight", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print bmi, category

function validate_input(prompt, min, max)
    print prompt
    get valid_input
    while valid_input < min or valid_input > max
        print "invalid input", prompt
        get valid-input
    return valid_input

function calculate_bmi(height, weight)
    return weight / (height ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return underweight
    else if bmi < 25
        return normal
    else if bmi < 30
        return overweight
    else
        return obese

main()
"""

def main():
    height = validate_input("Height (m): ", 0, 3)
    weight = validate_input("Weight (kg): ", 0, 100)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi:.1f}, which is considered {category}")

def validate_input(prompt,min, max):
    valid_input = float(input(prompt))
    while valid_input < min or valid_input > max:
        print("Invalid input")
        valid_input = float(input(prompt))
    return valid_input

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"

main()

