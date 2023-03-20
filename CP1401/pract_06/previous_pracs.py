# Calculate salary for worker level
"""
function main()
    worker_level = validate_input("worker level", 1, 10)
    total_pay = worker_level * 5000
    print worker_level, total_pay

function validate_input(prompt, min, max)
    print prompt
    get valid_input
    while valid_input < min or valid_input > max
        print "invalid input", prompt
        get valid-input
    return valid_input
"""
MINIMUM_WORKER_LEVEL = 1
MAXIMUM_WORKER_LEVEL = 10
PAY_MULTIPLIER = 5000
def main():
    worker_level = validate_input("What is the worker level? 1-10: ", 1, 10)
    total_pay = calculate_total_pay(worker_level)
    print(f"With worker level {worker_level}, your salary is ${total_pay:,.2f}")

def validate_input(prompt,min, max):
    valid_input = float(input(prompt))
    while valid_input < min or valid_input > max:
        print("Invalid input")
        valid_input = float(input(prompt))
    return valid_input

def calculate_total_pay(worker_level):
    return worker_level * PAY_MULTIPLIER

main()

# Print grid(rows, columns)
"""
function main()
    rows = validate_input("rows", 0)
    columns =  validate_input("columns", 0)
    print columns
    repeat rows times

    print worker_level, total_pay
get rows
get columns
repeat rows times
"""

def main():
    columns = validate_input("How many rows?: ", 0) #only uses a minimum, the grid has no max size limit
    rows = validate_input("How many columns?: ", 0)
    for r in range(rows):
        for c in range(columns):
            print(c, end=" ")
        print()

def validate_input(prompt,min):
    valid_input = int(input(prompt))
    while valid_input < min:
        print("Invalid input")
        valid_input = int(input(prompt))
    return valid_input

main()