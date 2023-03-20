"""
CP1401 2022-2 Assignment 1
Program 2 – Space Cadet
Student Name: Anastasia Eremenko
Date started: 20/12/2022

Pseudocode:

get practical_score
while practical_score > 50 or practical_score <0
    print error
    get practical_score
get exam_score
while exam_score > 50 or exam_score <0
    print error
    get exam_score
total_score = practical_score + exam_score
if total_score < 50
    print fail
else if total_score >= 90
    print honour roll
else if practical_score >= exam_score
    print field agent
else
    print desk officer
"""

INTRO = "Welcome Trainee Space Cadet. How did you do?"
PASS = 50
HONOUR = 90

print(INTRO)
practical_score = float(input("Practical score (0-50): "))
exam_score = float(input("Exam score (0-50): "))
total_score = int(practical_score + exam_score)  # uses an int type as example output showed integer total values
if total_score < PASS:
    result = "You failed. Please try again next year."
elif total_score >= HONOUR:
    result = "Congratulations on making the honour roll!"
elif practical_score >= exam_score:
    result = "You will become a field agent."
else:
    result = "You will become a desk officer."
print(f"Your total score is {total_score} out of 100.")
print(result)
