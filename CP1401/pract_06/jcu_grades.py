#3. JCU Grades

"""
function main()
    score = validate_score("Score", 0, 100)
    grade = calculate_grade(score)
    print score, grade

function validate_score(prompt, min, max)
    print prompt
    get valid_score
    while valid_score < min or valid_score > max
        print "invalid input", prompt
        get valid_score
    return valid_score

function calculate_grade(score)
    if score >= 85
        return HD
    else if score >= 75
        return D
    else if score >= 65
        return C
    else if score >= 50
        return P

main()
"""
import random

def main():
    score = validate_score("Score: ", 0, 100)
    grade = determine_grade(score)
    print(f"The score {score} is {grade}")
    number_of_scores = int(validate_score("How many random scores?: ", 0, 100))
    for rand_score in (range(number_of_scores)):
        rand_score = random.randint(1, 100)
        grade = determine_grade(rand_score)
        print(f"The score {rand_score} is {grade}")

def get_random_score(rand_score):
    rand_score = random.randint(1, 100)
    return rand_score

def random_grades(number_scores):
    for number in (range(0,number_scores-1)):
        print(number)

def validate_score(prompt, min, max):
    valid_score = float(input(prompt))
    while valid_score < min or valid_score > max:
        print("Invalid input")
        valid_score = float(input(prompt))
    return valid_score

def determine_grade(score):
    score = int(score)
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"

main()