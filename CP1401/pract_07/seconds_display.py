# 3. Seconds Display

"""
MIN_RANGE = 0
MAX_RANGE = 3176
STEP = 635

function main()
    for total_seconds in range(MIN_RANGE, MAX_RANGE, STEP)
        minutes = calculate_minutes(total_seconds)
        remainder_seconds = calculate_seconds(total_seconds, minutes)
        statement = format_string(total_seconds, minutes, remainder_seconds)
        print statement

function calculate_minutes(total_seconds)
    return int(total_seconds/60)

function calculate_seconds(total_seconds, minutes)
    return = total_seconds - minutes * 60

function format_string(total_seconds, minutes, remainder_seconds)
    return "total_seconds, minutes, remainder_seconds"
"""

MIN_RANGE = 0
MAX_RANGE = 3176
STEP = 635


def main():
    """Displays a range of seconds converted to min and sec format"""
    for total_seconds in range(MIN_RANGE, MAX_RANGE, STEP):
        minutes = calculate_minutes(total_seconds)
        remainder_seconds = calculate_seconds(total_seconds, minutes)
        statement = format_string(total_seconds, minutes, remainder_seconds)
        print(statement, sep=" ")


def calculate_minutes(total_seconds):
    """Calculates the number of minutes in the total seconds duration"""
    return int(total_seconds/60)


def calculate_seconds(total_seconds, minutes):
    """Calculates the number of seconds remaining from the total seconds"""
    return total_seconds - minutes * 60


def format_string(total_seconds, minutes, remainder_seconds):
    """Returns a fully formatted string displaying total seconds, min, sec"""
    return f"{total_seconds} seconds is {minutes}m and {remainder_seconds}s"


main()
