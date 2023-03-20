"""
CP1401 2023-2 Assignment 2
Market Garden Simulator
Student Name: Anastasia Eremenko
Date started: 30/1/2023

Pseudocode:
get random
MIN_RAIN = 0
MAX_RAIN = 128
LOW_RAIN_THRESHOLD = 32
INTRO_MESSAGE = "Rules and intro message"
MENU_OPTIONS = "(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: "
DEFAULT_PLANTS = ["Parsley", "Sage", "Rosemary", "Thyme"]

function main()
    display INTRO_MESSAGE
    get starting_plants("Would you like to load your plants from plants.txt (Y/n)?: ")
    food = 0
    days = 0
    display_my_plants(plants)
    display_current_status(days, plants, food)
    menu_choice = verify_menu(MENU_OPTIONS, days, plants, food)
    if menu_choice is A
        food_cost = add_new_plant(plants, food)
        food = food - food_cost
    if menu_choice is D
        display_my_plants(plants)
    if menu_choice is W
        days = days + 1
        food_produced = wait(days, plants)
        food = food + food_produced
    while menu_choice is not Q
        display_current_status(days, plants, food)
        menu_choice = verify_menu(MENU_OPTIONS, days, plants, food)
            if menu_choice is A
                food_cost = add_new_plant(plants, food)
                food = food - food_cost
            if menu_choice is D
                display_my_plants(plants)
            if menu_choice is W
                days = days + 1
                food_produced = wait(days, plants)
                food = food + food_produced
    if length plants >= 1
        display "You finished with these plants: "
        display_my_plants(plants)
    else
        display "You finished with no plants."
    display_current_status(days, plants, food)
    choose_save("Would you like to save your plants to plants.txt (Y/n)?:")
    if choose_save is True
        out_file(plants)
        display "Saved."
    display "Thank you for simulating. Now enjoy some real plants"

function choose_starting_plants(prompt)
    get response
    response = response uppercase
    if response != N
        starting_plants = DEFAULT_PLANTS
    else
        starting_plants = process(plants.txt)
    return starting_plants

function add_new_plant(plants, food)
    new_plant = string(if_duplicate_plant(string_not_empty("What plant do you want to buy?: "), plants))
    plant_cost = length(new_plant)
    if food < plant_cost
        display "new_plant would cost plant_cost food. With only food, you can't afford it.")
        return 0
    else
        append into plants(new_plant title case)
        food_cost = length(new_plant)
        return food_cost


function if_duplicate_plant(new_plant, plants)
    duplicate = False
    for plant in plants
        if string new_plant title case == string plant:
            duplicate = True
    while duplicate:
        duplicate = False
        display "You already have new_plant"
        new_plant = string_not_empty("What plant do you want to buy?: ")
        for plant in plants:
            if string new_plant title case == string plant:
                duplicate = True
    return new_plant

function wait(days, plants)
    days = days + 1
    rainfall = get_rainfall()
    display rainfall in mm
    display_if_dead(rainfall, plants)
    food = food_production(plants, rainfall)
    return food

function get_rainfall
    return random integer(MIN_RAIN, MAX_RAIN)

function display_if_dead(rainfall, plants)
    if rainfall < LOW_RAIN_THRESHOLD
        dead_plant = is_dead(plants)
        display "Sadly, your dead_plant plant has died."
        remove dead_plant from plants

function is_dead(plants)
    rand_num = random integer(0, length plants - 1)
    dead_plant = plants[rand_num]
    return dead_plant

function food_production(plants, rainfall)
    total_food_produced = 0
    if rainfall >= LOW_RAIN_THRESHOLD
        percent = get_percent(rainfall)
        for plant in plants
            food_produced = get_food_produced(percent, plant)
            total_food_produced += food_produced
            display plant produced food_produced
            plant_num = plant_num+ 1
    else
        for plant in plants
            display "plant produced 0"
    return total_food_produced

function get_percent(rainfall)
    percent = (random integer(integer(rainfall / 3), rainfall)) / MAX_RAIN
    return percent

function get_food_produced(percent, plant)
    return integer(percent * length(plant))

function verify_menu(prompt, days, plants, food)
    get choice
    choice = choice upper case
    while choice != W and choice != D and choice != A and choice != Q
        display "Invalid Choice"
        display_current_status(days, plants, food)
        get choice
        choice = choice upper case
    return choice

function string_not_empty(prompt)
    get response
    while length(response) <= 0
        display "Cannot be a blank name"
        get response
    return response

function display_current_status(days, plants, food)
    display "After x days, you have x plants and your total food is x."

function display_my_plants(items)
    for item in items
        display item

function process(in_file)
    lines = []
    in_file = open in_file for reading
    for line in in_file
        append into lines(stripped line)
    close in_file
    return lines

function choose_save(prompt)
    get choice
    choice = choice upper case
    if choice != N
        return True
    else
        return

function out_file(plants)
    plant_out_file = open plants.txt for writing
    for plant in plants
        display plant
    close plant_out_file
"""
import random

MIN_RAIN = 0
LOW_RAIN_THRESHOLD = 32
MAX_RAIN = 128
MENU_OPTIONS = "(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: "
INTRO_MESSAGE = "Welcome to my garden.\nPlants cost and generate food according to their name length " \
                "(e.g., Sage plants cost 4).\nYou can buy new plants with the food your garden generates.You get up " \
                "to 128 mm of rain per day.\nNot all plants can survive with less than 32.\nEnjoy :)"
DEFAULT_PLANTS = ["Parsley", "Sage", "Rosemary", "Thyme"]
FILE_NAME = "plants.txt"


def main():
    """Menu-driven program simulating plant growth, producing food based in rainfall and buying a new plants"""
    days = 0
    food = 0
    print(INTRO_MESSAGE)
    plants = choose_starting_plants(f"Would you like to load your plants from {FILE_NAME} (Y/n)?: ")
    display_list_items(plants)
    display_current_status(days, plants, food)
    menu_choice = verify_menu(MENU_OPTIONS, days, plants, food)
    if menu_choice == "A":
        food_cost = add_new_plant(plants, food)
        food -= food_cost
    if menu_choice == "D":
        display_list_items(plants)
    if menu_choice == "W":
        days += 1
        food_produced = wait(plants)
        food += food_produced
    while menu_choice != "Q":
        display_current_status(days, plants, food)
        menu_choice = verify_menu(MENU_OPTIONS, days, plants, food)
        if menu_choice == "A":
            food_cost = add_new_plant(plants, food)
            food -= food_cost
        if menu_choice == "D":
            display_list_items(plants)
        if menu_choice == "W":
            days += 1
            food_produced = wait(plants)
            food += food_produced
    if len(plants) >= 1:
        print("You finished with these plants: ")
        display_list_items(plants)
    else:
        print("You finished with no plants.")
    display_current_status(days, plants, food)
    choose_save(f"Would you like to save your plants to {FILE_NAME} (Y/n)?: ")
    if choose_save is True:
        out_file(plants)
        print("Saved.")
    print("Thank you for simulating. Now enjoy some real plants")


def choose_starting_plants(prompt):
    """Prompts the user to choose to load plants from a file or get default plants"""
    response = input(prompt)
    response.upper()
    if response != "N":
        starting_plants = DEFAULT_PLANTS
    else:
        starting_plants = process(FILE_NAME)
    return starting_plants


# The following functions relate to the "add new plant" menu option


def add_new_plant(plants, food):
    """Prompts the user to enter the name of the new plant and based on if they can afford it, buy it with food"""
    new_plant = str(if_duplicate_plant(string_not_empty("What plant do you want to buy?: "), plants))
    plant_cost = len(new_plant)
    if food < plant_cost:
        print(f"{new_plant} would cost {plant_cost} food. With only {food}, you can't afford it.")
        return 0
    else:
        plants.append(new_plant.title())
        food_cost = len(new_plant)
        return food_cost


def if_duplicate_plant(new_plant, plants):
    """Repeatedly prompts the user for a plant name until they enter one they do not own"""
    duplicate = False
    for plant in plants:
        if str(new_plant).title() == str(plant):
            duplicate = True
    while duplicate:
        duplicate = False
        print(f"You already have {new_plant}")
        new_plant = string_not_empty("What plant do you want to buy?: ")
        for plant in plants:
            if str(new_plant).title() == str(plant):
                duplicate = True
    return new_plant


# The following functions relate to the "Wait" menu option


def wait(plants):
    """The wait menu option which prompts an increase in days, food production and rainfall """
    rainfall = get_rainfall()
    print(f"Rainfall: {rainfall}mm")
    display_if_dead(rainfall, plants)
    food = food_production(plants, rainfall)
    return food


def get_rainfall():
    """Randomly assigns a rainfall amount based on min and max rain constants"""
    return random.randint(MIN_RAIN, MAX_RAIN)


def display_if_dead(rainfall, plants):
    """Displays the dead plant message if the rainfall is below low rain threshold"""
    if rainfall < LOW_RAIN_THRESHOLD:
        dead_plant = is_dead(plants)
        print(f"Sadly, your {dead_plant} plant has died.")
        plants.remove(dead_plant)


def is_dead(plants):
    """Randomly decides which plant will die and returns the name of the plant"""
    rand_num = random.randint(0, len(plants) - 1)
    dead_plant = plants[rand_num]
    return dead_plant


def food_production(plants, rainfall):
    """Decides the output displayed for function wait based on rainfall amount"""
    plant_num = 0  # Used in deciding punctuation
    total_food_produced = 0
    if rainfall >= LOW_RAIN_THRESHOLD:
        percent = get_percent(rainfall)
        for plant in plants:
            food_produced = get_food_produced(percent, plant)
            total_food_produced += food_produced
            print(f"{plant} produced {food_produced}", end="")
            punctuation(plant_num, plants)
            plant_num += 1
    else:
        for plant in plants:
            print(f"{plant} produced 0", end="")
            punctuation(plant_num, plants)
            plant_num += 1
    return total_food_produced


def get_percent(rainfall):
    """Randomly assigns a percentage between 1/3 of the rain and the maximum rain"""
    percent = (random.randint(int(rainfall / 3), rainfall)) / MAX_RAIN
    return percent


def get_food_produced(percent, plant):
    """Gives the food produced based on the length of the plans and a random percentage"""
    return int(percent * len(plant))


# The following functions relate to choice verification


def verify_menu(prompt, days, plants, food):
    """Repeatedly prompts the user for a choice until choice is one of the menu options"""
    choice = input(prompt)
    choice = choice.upper()
    while choice != "W" and choice != "D" and choice != "A" and choice != "Q":
        print("Invalid Choice")
        display_current_status(days, plants, food)
        choice = input(prompt)
        choice = choice.upper()
    return choice


def string_not_empty(prompt):
    """Error checks if the string is not empty, while empty repeats the input prompt"""
    response = input(prompt)
    while len(response) <= 0:
        print("Cannot be a blank name")
        response = input(prompt)
    return response


# The following functions relate to formatting and displaying inputs


def display_current_status(days, plants, food):
    """Displays the current status of the user, number of days passed, how many plants, food"""
    print(f"After {days} days, you have {len(plants)} plants and your total food is {food}.")


def display_list_items(items):
    """Displays all items in a list, in a single line, with appropriate punctuation"""
    item_num = 0  # is used to keep track of the item number to assign punctuation.
    for item in items:
        print(item, end="")
        punctuation(item_num, items)
        item_num += 1


def punctuation(item_num, items):
    """Adds on punctuation based on weather it's the last item (giving commas between and a dot at the end)"""
    if item_num != len(items) - 1:
        print(", ", end="")
    else:
        print(".")


# The following functions relate to reading an input file and writing to an output file


def process(in_file):
    """Reads the file and stores the lines in a list called plants"""
    lines = []
    in_file = open(in_file, 'r')
    for line in in_file:
        lines.append(line.strip())
    in_file.close()
    return lines


def choose_save(prompt):
    """Prompts the user if they want to save their plants, all and other than N are a yes"""
    choice = (input(prompt))
    choice.upper()
    if choice != "N":
        return True


def out_file(plants):
    """Reads the plants stored in the list (plants) and prints them to the designated out_file"""
    plant_out_file = open(FILE_NAME, "w")
    for plant in plants:
        print(plant, file=plant_out_file)
    plant_out_file.close()


main()
