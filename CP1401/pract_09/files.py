
#  4. Read a String from a File #########################################################################
def question_4():
    """Reads the name from the file and prints a greetings phrase"""
    file_name = "name.txt"
    text = process(file_name)
    print(f"Greetings {text}" + "!")


def process(file_name):
    in_file = open(file_name, "r")
    text = in_file.read().strip()
    in_file.close()
    return text


#  question_4()

#  5.Greater-Than Counter #########################################################################
def question_5():
    """Reads the numbers line by in a file and returns the percentage of numbers greater than the set threshold"""
    file_name = str(input("File name (hint: recentrain.txt): "))
    user_threshold = float(get_valid_number("Select Threshold: "))
    numbers = process(file_name)
    greater_than_count = how_many_greater_than(numbers, user_threshold)
    percent_greater = percentage_greater_than(greater_than_count, numbers)
    print(f"{greater_than_count} out of {len(numbers)} values in {file_name} "
          f"({percent_greater:.1f}%) are greater than {user_threshold}.", sep=" ")


def get_valid_number(prompt):
    """Validates that the number input is numeric"""
    valid_number = input(prompt)
    while not valid_number.isnumeric:
        print("Invalid input")
        valid_number = input(prompt)
    float(valid_number)
    return valid_number


def process(file_name):
    """Opens the files and stores each line as a numeric in a list (numbers)"""
    numbers = []
    in_file = open(file_name, "r")
    for line in in_file:
        number = float(line)
        numbers.append(number)
    in_file.close()
    return numbers


def how_many_greater_than(numbers, user_threshold):
    """Counts how many numbers out of the total lines are greater than the threshold"""
    number_of_greater_than = 0
    for number in numbers:
        if float(number) > user_threshold:
            number_of_greater_than += 1
    return number_of_greater_than


def percentage_greater_than(greater_than_count, numbers):
    """Calculates the percentage of numbers grater than the threshold"""
    return (greater_than_count / len(numbers)) * 100


# question_5()

#  6. File Filter #########################################################################
def question_6():
    """Takes an input file and searches for the user input search key, prints those lines in an output file"""
    in_file = input("In file (hint: letter.txt): ")
    search_key = input("Search key: ")
    user_out_file = input("Out file name: ")
    lines = process(in_file, search_key)
    process_out_file(user_out_file, lines)


def process(in_file, search_key):
    """Reads the file and stores the lines in a list"""
    lines = []
    in_file = open(in_file, 'r')
    for line in in_file:
        if line.find(search_key) >= 0:
            lines.append(line.strip())
    in_file.close()
    return lines


def process_out_file(user_out_file, lines):
    """Reads the lines stored in the list (lines) and prints them to the designated user_out_file"""
    out_file = open(user_out_file, "w")
    for line in lines:
        print(line, file=out_file)
    out_file.close()


#  question_6()
