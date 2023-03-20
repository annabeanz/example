"""
CP1401 2023-2 Assignment 2
Market Garden Simulator
Student Name: Anastasia Eremenko
Date started: 30/1/2023
Pseudocode:

"""
import random

MIN_RAIN = 0
LOW_RAIN_THRESHOLD = 32
MAX_RAIN = 33#128
MENU_OPTIONS = "(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: "
INTRO_MESSAGE = "Welcome to my garden.\nPlants cost and generate food according to their name length " \
                "(e.g., Sage plants cost 4).\nYou can buy new plants with the food your garden generates.You get up " \
                "to 128 mm of rain per day.\nNot all plants can survive with less than 32.\nEnjoy :)"
DEFAULT_PLANTS = ["Parsley", "Sage", "Rosemary", "Thyme"]
FILE_NAME = "plants.txt"


def main():
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
        food_produced = wait(days, plants)
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
            food_produced = wait(days, plants)
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


def wait(days, plants):
    days += 1
    rainfall = get_rainfall()
    print(f"Rainfall: {rainfall}mm")
    display_if_dead(rainfall, plants)
    food = food_production(plants, rainfall)
    return food


def get_rainfall():
    return random.randint(MIN_RAIN, MAX_RAIN)


def display_if_dead(rainfall, plants):
    if rainfall < LOW_RAIN_THRESHOLD:
        dead_plant = is_dead(plants)
        print(f"Sadly, your {dead_plant} plant has died.")
        plants.remove(dead_plant)


def is_dead(plants):
    rand_num = random.randint(0, len(plants) - 1)
    dead_plant = plants[rand_num]
    return dead_plant


def food_production(plants, rainfall):
    plant_num = 0
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
    percent = (random.randint(int(rainfall / 3), rainfall)) / MAX_RAIN
    return percent


def get_food_produced(percent, plant):
    return int(percent * len(plant))


# The following functions relate to choice verification


def verify_menu(prompt, days, plants, food):
    """Repeatedly prompts the user for a choice until choice meets 4 parameters"""
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
    print(f"After {days} days, you have {len(plants)} plants and your total food is {food}.")


def display_list_items(items):
    """Displays all items in a list, in a single line, with appropriate punctuation"""
    item_num = 0  # is used to keep track of the item number to assign punctuation.
    for item in items:
        print(item, end="")
        punctuation(item_num, items)
        item_num += 1


def punctuation(item_num, items):
    if item_num != len(items) - 1:
        print(", ", end="")
    else:
        print(".")


# The following functions relate to reading an input file and writing to an output file


def process(in_file):
    """Reads the file and stores the lines in a list"""
    lines = []
    in_file = open(in_file, 'r')
    for line in in_file:
        lines.append(line.strip())
    in_file.close()
    return lines


def choose_save(prompt):
    choice = (input(prompt))
    choice.upper()
    if choice != "N":
        return True
    else:
        return


def out_file(plants):
    """Reads the plants stored in the list (plants) and prints them to the designated out_file"""
    plant_out_file = open(FILE_NAME, "w")
    for plant in plants:
        print(plant, file=plant_out_file)
    plant_out_file.close()


main()
