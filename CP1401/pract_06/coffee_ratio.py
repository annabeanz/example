# 1. Coffee Brew Ratio
"""
function main()
    dose = validate_input("dose", 0 ,)
    yield = validate_input("yield", 0 ,)
    ratio = calculate_ratio(dose, yield)
    category = determine_category(ratio)
    print(ratio, category)

function validate_input(prompt, min, max)
    print prompt
    get valid_input
    while valid_input < min or valid_input > max
        print invalid input, prompt
        get valid-input
    return valid_input

function = calculate_ratio
    get dose, yield
    ratio = yield / dose
    print ratio

function determine_category(ratio)
    if ratio < 1
        return "Invalid"
    else if ratio >= 2
        return "ristretto"
    else if ratio >= 3
        return "normale"
    else if ratio >= 4
        return "lungo"
    else
        return
"""

# 1. Coffee Brew Ratio
def main():
    dose = validate_input("Dose (g): ", 0)
    coffee_yield = validate_input("Coffee yield (g): ", 0)
    ratio = calculate_ratio(dose, coffee_yield)
    category = determine_category(ratio)
    print(f"""Dose: {dose}
Yield: {coffee_yield}
1:{ratio:.1f} is considered {category}""")

def validate_input(prompt,min):
    valid_input = float(input(prompt)) #no maximum as the same rules still apply to large numbers
    while valid_input < min:
        print("Invalid input")
        valid_input = float(input(prompt))
    return valid_input

def calculate_ratio(dose, coffee_yield):
    return coffee_yield / dose

def determine_category(ratio):
    if ratio < 2:
        return "ristretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"

def check_coffee():
    category = determine_category(1)
    print(category, end=" ")
    print("-> this should be ristretto")
    category = determine_category(2)
    print(category, end=" ")
    print("-> this should be normale")
    category = determine_category(13.5)
    print(category, end=" ")
    print("-> this should be lungo")

check_coffee()
#call the above function to conduct a test of the code

main()