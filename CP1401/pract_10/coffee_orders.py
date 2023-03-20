#  All Together Now
"""
WELCOME_MESSAGE = "Welcome to the IT@JCU Coffee Shop"
MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit: "
ORDER_CHOICES = "Please choose from:\nFlat White - Espresso - Long Black - Babyccino - ?: "
BABYCCINO_INSTRUCTONS = string instructions unique to babyccino
FLAT_WHITE_INSTRUCTONS =  string instructions unique to flat white
ESPRESSO_INSTRUCTIONS =  string instructions unique to espresso
LONG_BLACK_INSTRUCTONS =  string instructions unique to long black

function main():
    ordered_coffee = []
    menu_choice = validate_option(MENU, "Order", "Drink", "Random", "Quit", "Invalid")
    execute_choice(menu_choice, ordered_coffee)
    while menu_choice != "Quit":
        menu_choice = validate_option(MENU, "Order", "Drink", "Random", "Quit", "Invalid")
        execute_choice(menu_choice, ordered_coffee)
    display "Thanks for drinking coffee"

function validate_option(prompt, option_1, option_2, option_3, option_4, invalid_msg):
    get choice
    while (choice != option_1) and (choice != option_2) and (choice != option_3) and (choice != option_4):
        display invalid_msg
        get choice
    return choice

function execute_choice(menu_choice, ordered_coffee):
    if menu_choice == "O":
        coffee_choice = validate_option(ORDER_CHOICES, "Flat white", "Espresso", "Long Black", "Babyccino",
                                        "Invalid")
        ordered_coffee append to coffee_choice
        instructions = get_instructions(coffee_choice)
        display instructions
    else if menu_choice == "D":
        drinking_output(ordered_coffee)
        clear ordered_coffee
    else if menu_choice == "R":
        coffee_choice = get_random_coffee()
        ordered_coffee append to coffee_choice
        instructions = get_instructions(coffee_choice)
        display(instructions)

function get_instructions(coffee_choice):
    if coffee_choice == "Flat white":
        output = SHARED_LINES + FLAT_WHITE_LINES
    else if coffee_choice == "Espresso":
        output = SHARED_LINES
    else if coffee_choice == "Long black":
        output = SHARED_LINES + LONG_BLACK_LINES
    else
        output = BABYCCINO_LINES
    return Here's how to make a coffee_choice, output

function drinking_output(ordered_coffee):
    if len(ordered_coffee) == 0:
        display("Oh... where's my coffee?")
    for coffee in ordered_coffee:
        display Mmm, nice coffee

function get_random_coffee():
    choice = random.randint(1, 4)
    if choice == 1:
        order = "Espresso"
    else if choice == 2:
        order = "Babyccino"
    else if choice == 3:
        order = "Long Black"
    else:
        order = "Flat white"
    return order

main()
"""
import random

WELCOME_MESSAGE = "Welcome to the IT@JCU Coffee Shop"
MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit: "
ORDER_CHOICES = "Please choose from:\nFlat White - Espresso - Long Black - Babyccino - ?: "

SHARED_LINES = "- Insert portafilter into grinder\n- Press grind button to grind beans into portafilter\n- Distribute" \
               " grounds\n- Tamp grounds\n- Insert full portafilter into group head\n- Press shot button to pour " \
               "espresso into cup"
FLAT_WHITE_LINES = "- Fill jug with milk\n- Steam milk until nice microfoam formed and milk up to temperature\n- " \
                   "Swirl milk gently in jug\n- Pour milk into cup... carefully, artistically :)"
LONG_BLACK_LINES = "- Add hot water to cup"
BABYCCINO_LINES = "- Fill jug with milk\n- Steam milk until nice microfoam formed and milk up to temperature\n- " \
                  "Swirl milk gently in jug\n- Pour milk and foam into small cup... carefully\n- Gently " \
                  "sprinkle cinnamon atop foam"


def main():
    """A menu-run program that asks the user for a coffee choice and presents instructions, the user can drink it"""
    ordered_coffee = []  # stored all coffee orders and clears when drank
    menu_choice = validate_option(MENU, "O", "D", "R", "Q", "Invalid option")
    execute_choice(menu_choice, ordered_coffee)
    while menu_choice != "Q":
        menu_choice = validate_option(MENU, "O", "D", "R", "Q", "Invalid option")
        execute_choice(menu_choice, ordered_coffee)
    print("Thanks for drinking coffee")


def validate_option(prompt, option_1, option_2, option_3, option_4, invalid_msg):
    """Repeatedly prompts the user for a choice until choice meets 4 parameters"""
    choice = input(prompt)
    choice = choice.upper()
    while choice != option_1 and choice != option_2 and choice != option_3 and choice != option_4:
        print(invalid_msg)
        choice = input(prompt)
        choice = choice.upper()
    return choice


def execute_choice(menu_choice, ordered_coffee):
    """Executes menu options (Order)(Drink) and (Random), allowing user to order and drink coffee"""
    if menu_choice == "O":
        coffee_choice = validate_option(ORDER_CHOICES, "FLAT WHITE", "ESPRESSO", "LONG BLACK", "BABYCCINO",
                                        "Invalid order")
        ordered_coffee.append(coffee_choice)
        instructions = get_instructions(coffee_choice)
        print(instructions)
    elif menu_choice == "D":
        drinking_output(ordered_coffee)
        ordered_coffee.clear()
    elif menu_choice == "R":
        coffee_choice = get_random_coffee()
        ordered_coffee.append(coffee_choice)
        instructions = get_instructions(coffee_choice)
        print(instructions)


def get_instructions(coffee_choice):
    """Returns the step-by-step instructions for each respective coffee type"""
    if coffee_choice == "FLAT WHITE":
        output = SHARED_LINES + FLAT_WHITE_LINES
    elif coffee_choice == "ESPRESSO":
        output = SHARED_LINES
    elif coffee_choice == "LONG BLACK":
        output = SHARED_LINES + LONG_BLACK_LINES
    else:
        output = BABYCCINO_LINES
    return f"Here's how to make a/n {coffee_choice.title()}:\n{output}"


def drinking_output(ordered_coffee):
    """Prints a string based on the weather the user ordered coffee and what type"""
    if len(ordered_coffee) == 0:
        print("Oh... where's my coffee?")
    for coffee in ordered_coffee:
        print(f"Mmm, nice {coffee.title()}")


def get_random_coffee():
    """Returns a random coffee order out of the available 4"""
    choice = random.randint(1, 4)
    if choice == 1:
        order = "ESPRESSO"
    elif choice == 2:
        order = "BABYCCINO"
    elif choice == 3:
        order = "LONG BLACK"
    else:
        order = "FLAT WHITE"
    return order


main()
