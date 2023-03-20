"""
CP1401 2022-2 Assignment 1
Program 3 – Sleep Tracker
Student Name: Anastasia Eremenko
Date started: 21/12/2022

Pseudocode:

NUMBER_NIGHTS = 5
RECOMMENDED_SLEEP_NIGHTLY = 8
current_night = 1
total_hours = 0
for night in range(NUMBER_NIGHTS)
    get hours_slept
    while hours_slept > 24 or hours_slept < 0
        print error
        get hours_slept
    current_night + 1
    total_hours += hours_slept
recommended_total_sleep = NUMBER_NIGHTS * RECOMMENDED_SLEEP_NIGHTLY
if recommended_total_sleep > total_hours
    debt = recommended_total_sleep - total_hours
else
    debt = "enough sleep"
print recommended_total_sleep, total_hours, debt
"""

NUMBER_NIGHTS = 5
RECOMMENDED_SLEEP_NIGHTLY = 8
current_night = 1
total_hours = 0
for night in range(NUMBER_NIGHTS):  # used a "for" loop to be able to adjust the number of nights
    hours_slept = float(input(f"Night {current_night} hours sleep: "))
    while hours_slept > 24 or hours_slept < 0:  # while loop repeats till a valid input is given
        print("Invalid number of hours.")
        hours_slept = float(input(f"Night {current_night} hours sleep: "))
    current_night += 1
    total_hours += hours_slept
recommended_total_sleep = NUMBER_NIGHTS * RECOMMENDED_SLEEP_NIGHTLY
if recommended_total_sleep > total_hours:  # if, else statement is used to separate comments based on sleep debt
    debt = recommended_total_sleep - total_hours
    debt_comment = f"Your sleep debt over this time is: {debt}"
else:
    debt_comment = "You are getting enough sleep. Keep it up!"
print(f"""Recommended total sleep is: {recommended_total_sleep}
Your total hours of sleep: {total_hours:,.2f}
{debt_comment}""", sep=" ")
