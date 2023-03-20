""" CP1401 2022-2 Assignment 1 Program 1 – Pay Calculator
Student Name: Anastasia Eremenko
Date started: 19/12/2022

Pseudocode:

BASE_PAY = 45
PER_LEVEL_INCREASE = 0.05
function main()
    hours_worked = validate_input("hours", 0)
    worker_level = validate_input("level", 0)
    hourly_pay = calculate_hourly_pay(worker_level)
    total_pay = calculate_total_pay(hourly_pay, hours_worked)
    print worker_level, hourly_pay, total_pay

main()

experience level 0 is $45.00
Each level of experience gives 5% more pay,
"""
INTRO = "Experience Counts Pay Calculator"
BASE_PAY = 45
PER_LEVEL_INCREASE = 0.05
def main():
    print(INTRO)
    hours_worked = validate_input("Number of hours worked: ", 0)
    experience_level = validate_input("Experience level: ", 0)
    hourly_rate = calculate_rate(experience_level)
    total_pay = calculate_pay(hourly_rate,hours_worked)
    print(f"""Based on your experience level ({experience_level}):
    Your hourly pay rate is ${hourly_rate:,.2f}
    Your total pay is ${total_pay:,.2f}""", sep=" ")

def validate_input(prompt,min):  #no maximum required
    valid_input = float(input(prompt))
    while valid_input < min:
        print("Invalid input")
        valid_input = float(input(prompt))
    return valid_input

def calculate_rate(experience_level):
    hourly_rate = (1 + experience_level * PER_LEVEL_INCREASE) * BASE_PAY
    return hourly_rate

def calculate_pay(hourly_rate,hours_worked):
    total_pay = hourly_rate * hours_worked
    return total_pay

main()


