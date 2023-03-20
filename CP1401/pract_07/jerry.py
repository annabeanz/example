"""
MILE_TO_KILOMETER_COEFFICIENT = 1.609344

function main
    speed_in_mph = get_valid_number("speed in mph", 0)
    speed_limit_in_kph = get_valid_number("speed limit in kph", 0)
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over = calculate_speed_over(speed_in_km, speed_limit_in_kph)
    fine, message = determine_fine(speed_over)
    print fine, message

function get_valid_number(prompt, max)
    print prompt
    get valid_number
    while valid_number > max
        print "invalid input", prompt
        get valid_number
    return valid_number

function convert_miles_to_km
    number_of_miles = number_of_kilometers * MILE_TO_KILOMETER_COEFFICIENT
    return number_of_kilometers

function calculate_speed_over(speed_in_km, speed_limit_in_kph)
    return speed_in_km - speed_limit_in_kph

function determine_fine(speed_over)
    if speed_over < 0:
        infringement = 0
        message = "not over the limit"
    else if speed_over < 13:
        infringement = 177
    else if speed_over < 20:
        infringement = 266
    else if speed_over < 30:
        infringement = 444
    else if speed_over < 40:
        infringement = 622
    else if speed_over < 40:
        infringement = 1245
    return infringement,message

main()
"""

MILE_TO_KILOMETER_COEFFICIENT = 1.609344
FINE_MESSAGE = f"You are over the limit, your fine is $"


def main():
    """Determiner of a fine with a mph input and a kph speed limit"""
    speed_in_mph = get_valid_number("Speed in mph: ", 0)
    speed_limit_in_kph = get_valid_number("Speed limit in kph: ", 0)
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over = calculate_speed_over(speed_in_kph, speed_limit_in_kph)
    fine, message = determine_fine(speed_over)
    print(message, fine, sep="")


def get_valid_number(prompt, min):
    """Validate that the input is above minimum"""
    valid_number = float(input(prompt))
    while valid_number < min:
        print("Invalid input")
        valid_number = float(input(prompt))
    return valid_number


def convert_miles_to_km(speed_in_mph):
    """Convert miles to kilometers"""
    number_of_kilometers = speed_in_mph * MILE_TO_KILOMETER_COEFFICIENT
    return number_of_kilometers


def calculate_speed_over(speed_in_km, speed_limit_in_kph):
    """Calculates the speed over the speed limit in kph"""
    return speed_in_km - speed_limit_in_kph


def determine_fine(speed_over):
    """Returns the fine price as an integer and which message will be displayed according to the fine"""
    if speed_over < 0:
        infringement = 0
        message = "You are not over limit your fine is $"
    elif speed_over < 13:
        infringement = 177
        message = FINE_MESSAGE
    elif speed_over < 20:
        infringement = 266
        message = FINE_MESSAGE
    elif speed_over < 30:
        infringement = 444
        message = FINE_MESSAGE
    elif speed_over < 40:
        infringement = 622
        message = FINE_MESSAGE
    elif speed_over < 40:
        infringement = 1245
        message = FINE_MESSAGE
    return infringement, message  # infringement and message are separated so that the integer is preserved


main()
