#  2. Dog years
"""
BREAK = 0
EXIT = "GOOD BYE"

function main()
    human_years = get_human_years("Human years: ")
    while human_years >= BREAK
        dog_years = calculate_dog_years(human_years)
        print dog_years
        human_years = get_human_years("Human years: ")
    print EXIT

function get_human_years(prompt)
    print prompt
    get human years
    return human_years

function calculate_dog_years
    if human_years <= 2
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)
    return dog_years
"""

BREAK = 0
EXIT = "GOOD BYE"


def main():
    human_years = get_human_years("Human years: ")
    while human_years >= BREAK:
        dog_years = calculate_dog_years(human_years)
        print(dog_years)
        human_years = get_human_years("Human years: ")
    print(EXIT)


def get_human_years(prompt):
    human_years = int(input(prompt))
    return human_years


def calculate_dog_years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)
    return dog_years


main()
