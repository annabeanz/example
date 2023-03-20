# 1. Random Numbers
"""
MIN = 0
MAX = 100

get quantity_numbers
numbers = empty list
    get random number between MIN and MAX
    append into numbers
    repeat quantity_numbers times
print numbers
"""
import random

LOWEST = 0
numbers=[]

quantity_numbers = int(input("How many numbers?: "))
largest = int(input("What is the maximum number?: "))
for number in range(quantity_numbers):
    number = random.randint(LOWEST, largest)
    numbers.append(number)
randomly_chosen_index = random.randint(0, len(numbers))
print("The numbers are: ", numbers)
print("The minimum is: ", min(numbers))
print("The maximum is: ", max(numbers))
print("A randomly chosen number is: ", numbers[randomly_chosen_index])
numbers.reverse()
print(f"The numbers reversed are: {numbers}")
numbers.sort()
print(f"The numbers sorted are: {numbers}")
