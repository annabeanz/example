"""
CP1401 2022-2 Assignment 1
Program 1 – Pay Calculator
Student Name: Anastasia Eremenko
Date started: 19/12/2022

Pseudocode:

BASE_PAY = 45
PER_LEVEL_INCREASE = 0.05
get hours_worked
while hours_worked < 0
    print error
    get hours_worked
get worker_level
while worker_level < 0
    print error
    get worker_level
hourly_rate = (1 + experience_level * PER_LEVEL_INCREASE) * BASE_PAY
total_pay = hourly_rate * hours_worked
print worker_level, hourly_pay, total_pay
"""

INTRO = "Experience Counts Pay Calculator"
BASE_PAY = 45
PER_LEVEL_INCREASE = 0.05

print(INTRO)
hours_worked = float(input("Number of hours worked: "))
while hours_worked < 0:
    print("Invalid input")
    hours_worked = float(input("Number of hours worked: "))
experience_level = int(input("Experience level: "))  # experience level can only be an integer value
while experience_level < 0:
    print("Invalid input")
    experience_level = float(input("Experience level: "))

hourly_rate = (1 + experience_level * PER_LEVEL_INCREASE) * BASE_PAY
total_pay = hourly_rate * hours_worked
print(f"""Based on your experience level ({experience_level}):
Your hourly pay rate is ${hourly_rate:,.2f}
Your total pay is ${total_pay:,.2f}""", sep=" ")
