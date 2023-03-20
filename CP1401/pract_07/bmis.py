# 4. BMIs
"""
START_HEIGHT = 175
END_HEIGHT = 190
STEP_HEIGHT = 1

START_WEIGHT = 50
END_WEIGHT = 100
STEP_WEIGHT = 2

function main()
    for height in range(START_HEIGHT, END_HEIGHT, STEP_HEIGHT)
        for weight in range(START_WEIGHT, END_WEIGHT, STEP_WEIGHT)
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            statement = format_string(height, weight, bmi, category)
            print statement

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

function format_string(height, weight, bmi, category)
    return "height, weight, bmi, category"

main()
"""
START_HEIGHT = 150
END_HEIGHT = 190 + 1  # formatted so that the first number represents the end height in cm
STEP_HEIGHT = 10

START_WEIGHT = 50
END_WEIGHT = 100 + 1  # formatted so that the first number represents the end weight in kg
STEP_WEIGHT = 10


def main():
    """Displays a range of heights and weights and their corresponding BMI and BMI category"""
    for height in range(START_HEIGHT, END_HEIGHT, STEP_HEIGHT):
        for weight in range(START_WEIGHT, END_WEIGHT, STEP_WEIGHT):
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            statement = format_string(height, weight, bmi, category)
            print(statement)


def calculate_bmi(height, weight):
    """Calculates the BMI using height in m and weight in kl"""
    return weight / ((height/100) ** 2)


def determine_weight_category(bmi):
    """Returns the weight category according to the bmi"""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def format_string(height, weight, bmi, category):
    """Returns a fully formatted string displaying height,weight,bmi and category"""
    return f"Height {height/100}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category}"


main()
