#  1. Processing Strings #########################################################################
def question_1():
    """Takes a list of results strings and returns only the float value of the result """
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    for i in data_strings:
        extracted_number = extract_number(i)
        print(extracted_number)


def extract_number(i):
    """Extracts only the numbers between the = and the % sign and returns it as a float value"""
    equals_index = i.find("=")
    percent_index = i.find("%")
    number = float(i[equals_index + 2:percent_index])
    return number

#  question_1()


#  2. Date Strings #########################################################################
CURRENT_YEAR = 2023


def question_2():
    user_date = input("Date (dd/mm/yyyy): ")
    verified = match_date_pattern(user_date)
    while not verified:
        print("Invalid Format")
        user_date = input("Date (dd/mm/yyyy): ")
        verified = match_date_pattern(user_date)
    birth_date = user_date.split("/")
    current_age = CURRENT_YEAR - int(birth_date[2])
    print(f"DOB: {user_date}\nYou were born in: {birth_date[2]}\nYou will turn {current_age + 1} in {CURRENT_YEAR + 1}")


def match_date_pattern(user_date):
    """Error checks the user date input to match the format (dd/mm/yyyy)"""
    if user_date[2] == "/" and user_date[5] == "/" and user_date.replace("/", "").isdigit():
        return True
    else:
        return False


#  question_2()


#  3. Subject Code Strings #########################################################################
def question_3():
    """A program that takes the subject code and returns if it's an IT subject and the year of the subject"""
    user_code = get_valid_code("Enter subject code: ")
    year_string = year_comment(user_code)
    it_string = is_it(user_code)
    print(f"That is a {year_string}{it_string} subject.")


def get_valid_code(prompt):
    """Validate that the input year_lv and subject_type is in the correct format"""
    code = input(prompt)
    year_lv = code[2]
    subject_type = code[:2]
    while not year_lv.isdigit() and not subject_type.isnumeric():
        print("Invalid code")
        code = input(prompt)
        year_lv = code[2]
        subject_type = code[:2]
    return code


def is_it(code):
    """Adds on (IT) string if the subject is an IT subject (if it starts with CP)"""
    if code.startswith("CP"):
        return " IT"
    else:
        return ""


def year_comment(code):
    """Returns a string according to the year in the subject code"""
    year = int(code[2])
    if year == 1:
        return "first-year"
    elif year == 2:
        return "second-year"
    elif year == 3:
        return "third-year"
    elif year <= 5:
        return "Masters or Other"
    else:
        return "unregistered year"


#  question_3()
