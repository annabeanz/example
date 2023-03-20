#  1. Print a line ##############################################################
NUMBER_OF_HYPHENS = 40


def question_1():
    for i in range(NUMBER_OF_HYPHENS):
        print("-", end="")

# question_1()

# 2. Is it even? ##############################################################


def question_2():
    number = int(input("Number: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#  question_2()

#  3. Get Non-empty String #########################################################


def question_3():
    name = is_not_empty("Enter your name: ")
    country = is_not_empty("Enter where you are from: ")
    print()
    print(f"Hello {name} from {country}!")


def is_not_empty(prompt):
    user_input = input(prompt)
    while user_input == "":
        print("Nothing found")
        user_input = input(prompt)
    return user_input

#  question_3()

#  4. Number List


def question_4():
    lowest = int(input("Minimum number: "))
    highest = above_lowest("Maximum number: ", lowest)
    list_of_numbers = listing_numbers(lowest, highest)
    print(list_of_numbers)


def above_lowest(prompt, lowest):
    highest = int(input(prompt))
    while highest <= lowest:
        print(f"Your number must be greater than {lowest}", sep=" ")
        highest = int(input(prompt))
    return highest


def listing_numbers(lowest, highest):
    list_of_numbers = []
    for number in range(lowest, highest + 1):
        list_of_numbers.append(number)
    return list_of_numbers

#  question_4()

# 5. Subject List


def question_5():
    """A program that takes the subject code and returns if it's an IT subject and the year of the subject"""
    codes = []
    count = 0
    user_code = get_valid_code("Enter subject code: ")
    codes.append(user_code)
    while user_code != "":
        user_code = get_valid_code("Enter subject code: ")
        codes.append(user_code)
        count += 1
    print(f"\nYou take these {count} subject(s):"), display_codes(codes), if_cool(codes)


def get_valid_code(prompt):
    """Validates that the input year_lv and subject_type is in the correct format"""
    code = input(prompt)
    code_numbers = code[2:6]
    subject_type = code[:2]
    while code != "":
        while not code_numbers.isnumeric() or not subject_type.isalpha() or len(code) != 6:
            print("Invalid code")
            code = input(prompt)
            code_numbers = code[2:6]
            subject_type = code[:2]
        return code.upper()
    return code


def display_codes(codes):
    """Prints each code line by line stored in the list (codes)"""
    for code in codes:
        if code != "":
            print(code)


def if_cool(codes):
    """Prints the sting (you are cool) if the user inputs (CP1401)"""
    coolness = 0
    for code in codes:
        if code == "CP1401":
            coolness += 1
    if coolness > 0:
        print("You are cool")


# question_5()
