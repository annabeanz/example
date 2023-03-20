# 1. Error checking
"""
get worker_level
while input > 10 or input <1
    display error message
print worker_level * 5000
"""
MINIMUM_WORKER_LEVEL = 1
MAXIMUM_WORKER_LEVEL = 10
worker_level = int(input("What is the worker level? 1-10: "))
while worker_level < MINIMUM_WORKER_LEVEL or worker_level > MAXIMUM_WORKER_LEVEL:
    print("Please input a valid worker level")
    worker_level = int(input("What is the worker level? 1-10: "))
total_pay = worker_level * 5000
print(f"With worker level {worker_level}, your salary is ${total_pay:,.2f}")

# 2. Number sequences
for a in range(99, 0, -2):
    print(a)

for b in range(1896, 2022, 4):
    print(b, end=" ")
print()

for c in range(100, 0, -8):
    print(c, end=" ")
# Assuming I had 100 candies and I ate 8 each day, this code shows how many candies should I have each day.

# 3. Menus
# I have a question! in the code below I had to repeat user_response = ... 3 times
# however inputting user_response on its own causes the loop to be infinate
# how do I stop repeating it?
"""
S = :)
F = :(
get user_response capitalised
while (user_response != S) and (user_response != F) and (user_response != Q)
    display "please enter a valid input S F or Q"
    get user_response.upper
while user_response != Q
    if user_response == S
        display S
    if user_response == F
        display F
"""

S = ":)"
F = ":("
user_response = input("Smiley, Frowney or Quit? input S F or Q: ").upper()
while (user_response != "S") and (user_response != "F") and (user_response != "Q"):
    print("please enter a valid input")
    user_response = input("Please enter a valid response! S F or Q: ").upper()
while user_response != "Q":
    if user_response == "S":
        print(S)
    if user_response == "F":
        print(F)
    user_response = input("Smiley, Frowney or Quit? input S F or Q: ").upper()
print("Good Bye")

# 4. Accumulation

# AVERAGE AGE
""" 
total_people = 0
total_ages = 0
SENTINEL = done
while datalog != done
    get age_of_person
    total_ages = total_ages + age_of_person
    total_people = total_people + 1
mean_age = total_ages / total_people
display total_people, mean_ages
"""
total_people = 0
total_ages = 0
mean_age = 0
SENTINEL = "done"
print("Please type in the ages one by one and type 'done' when you are done.")
datalog_input = input(f"Please type the age of person {total_people + 1} : ")
while datalog_input != SENTINEL:
    total_ages = int(total_ages) + int(datalog_input)
    total_people = total_people + 1
    datalog_input = input(f"Please type the age of person {total_people + 1} : ")
    mean_age = total_ages / total_people
print(f"The total number of people recorded is {total_people} and the mean age is {mean_age}")

# SMILEYS COUNT (code used from "smileys" exercise)
S = ":)"
F = ":("
smileys_count = 0
frowney_count = 0
user_response = input("Smiley, Frowney or Quit? input S F or Q: ").upper()
while (user_response != "S") and (user_response != "F") and (user_response != "Q"):
    print("please enter a valid input")
    user_response = input("Please enter a valid response! S F or Q: ").upper()
while user_response != "Q":
    if user_response == "S":
        print(S)
        smileys_count += 1
    if user_response == "F":
        print(F)
        frowney_count += 1
    user_response = input("Smiley, Frowney or Quit? input S F or Q: ").upper()
print(f"You printed {smileys_count} smileys and {frowney_count} frowneys")
print("Good Bye")

#TOTAL NUMBERS
"""
SENTINEL = done
numbers_input = 0
while numbers_input != SENTINEL
    get numbers_input
    numbers_input += numbers_input
"""
SENTINEL = "done"
number_of_numbers = 0
numbers_totaled = 0
print("What numbers do you want to add up?")
numbers_input = input(f"Enter number {number_of_numbers + 1}: ")
while numbers_input != SENTINEL:
    number_of_numbers = number_of_numbers + 1
    numbers_totaled = numbers_totaled + int(numbers_input)
    numbers_input = input(f"Enter number {number_of_numbers + 1}: ")
print(f"The total of those {number_of_numbers} numbers is {numbers_totaled}")

# 5. Guessing game
"""
SECRET_NUMBER = 9
guesses = 0
get guess
while guess != SECRET_NUMBER:
    get guess
    guesses = guesses + 1
display guesses 
"""
SECRET_NUMBER = 9
guesses = 0
guess = int(input("Guess the number!: "))
while guess != SECRET_NUMBER:
    if guess > SECRET_NUMBER:
        print("Lower")
    if guess < SECRET_NUMBER:
        print("Higher")
    guess = int(input("Guess again!: "))
    guesses = guesses + 1
print(f"You took {guesses + 1} guesses to get it right")

# 6. Nested Loops
"""
get rows
get columns
repeat rows times
"""
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
for r in range(rows):
    for c in range(columns + 1):
        print(c, end=" ")
    print()