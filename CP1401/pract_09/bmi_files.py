# 7. BMI Files
"""
LOWEST = 0

function main():
    user_out_file = input("Name of the output file: ")
    user_number_people = int(get_valid_number("Number of people: ", LOWEST))
    bmis = []
    for person in range user_number_people
        person_number = person + 1
        height = get_valid_number(f"Height {person_number}: ", LOWEST)
        weight = get_valid_number(f"Weight {person_number}: ", LOWEST)
        bmi = calculate_bmi(height, weight)
        bmis append bmi
    out_file = process_out_file(user_out_file,bmis)
    in_file = process_in_file(user_out_file)

function calculate_bmi(height, weight)
    return weight / (height ** 2)

function process_out_file(user_out_file, bmis)
    out_file = open user_out_file for writing
    for bmi in bmis
        display(bmi, out_file)
    out_file.close()

function process_in_file(user_out_file)
    in_file = open user_out_file for reading
    for line in in_file
        bmi = float(line)
        category = determine_weight_category(bmi)
        statement = format_string(bmi, category)
        print(statement)
    in_file.close()

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
    return bmi, category

main()
"""
LOWEST = 0


def main():
    """Asks for number of people, and their respective heights and weights, displays BMI and category"""
    user_out_file = input("Name of the output file (hint bmis.txt): ")
    user_number_people = int(get_valid_number("Number of people: ", LOWEST))
    bmis = []
    for person in range(user_number_people):
        person_number = person + 1
        height = get_valid_number(f"Height in cm for person {person_number}: ", LOWEST)
        weight = get_valid_number(f"Weight in kg for person {person_number}: ", LOWEST)
        bmi = calculate_bmi(height, weight)
        bmis.append(bmi)
    out_file = process_out_file(user_out_file, bmis)
    print()
    in_file = process_in_file(user_out_file)


def get_valid_number(prompt, lowest):
    """Validate that the input is above minimum"""
    valid_number = float(input(prompt))
    while valid_number < lowest:
        print("Invalid input")
        valid_number = float(input(prompt))
    return valid_number


def calculate_bmi(height, weight):
    """Calculates the BMI using height in m and weight in kl"""
    return weight / ((height/100) ** 2)


def process_out_file(user_out_file, bmis):
    """Reads the bmis stored in the list (bmis) and prints them to the designated user_out_file"""
    out_file = open(user_out_file, "w")
    for bmi in bmis:
        print(bmi, file=out_file)
    out_file.close()


def process_in_file(user_out_file):
    """Takes bmis stored in user_out_file and prints statements based on the stored values"""
    in_file = open(user_out_file, 'r')
    for line in in_file:
        bmi = float(line)
        category = determine_weight_category(bmi)
        statement = format_string(bmi, category)
        print(statement)
    in_file.close()


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


def format_string(bmi, category):
    """Returns a fully formatted string displaying height,weight,bmi and category"""
    return f"BMI {bmi:.1f}, is considered {category}"


main()
