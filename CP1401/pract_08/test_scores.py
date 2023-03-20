# 2.Test Scores
"""
REPETITIONS = 4
grades = []
MIN_NUM = 0
MAX_NUM = 100

function main()
    scoreS = get random number between MIN_NUM and MAX_NUM
        append into numbers
        repeat REPETITIONS times
    grade = calculate_grade(score)
    print score, grade

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
REPETITIONS = 4
LOWEST = 0  # lowest and largest values are based on minimum and maximum grade boundaries
LARGEST = 100
scores = []


def main():
    """Function that takes an input REPETITIONS number of times, prints a grade for each and displays the average"""
    total_score = 0
    for score in range(REPETITIONS):
        score = validate_score("Score: ", LOWEST, LARGEST)
        scores.append(score)
    for score in scores:
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")
        total_score = total_score + score
    average_score = total_score / REPETITIONS
    trend = is_positive(average_score)
    print(f"The average score was {average_score}")
    print(trend)


def validate_score(prompt, lowest, largest):
    """Ensures the score inputted by the user is above the LOWEST and the LARGEST possible value"""
    valid_score = float(input(prompt))
    while valid_score < lowest or valid_score > largest:
        print("Invalid input")
        valid_score = float(input(prompt))
    return valid_score


def determine_grade(score):
    """Takes in scores out of 100 and determines the letter grade as assigned by JCU grading criteria"""
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


def is_positive(average_score):
    """Determines if the trend is positive. If the last value in list scores > average_score, trend is positive"""
    if scores[REPETITIONS - 1] > average_score:
        return "The trend is positive"
    else:
        return "The trend is negative"


main()
