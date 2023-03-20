"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(1, len(names)):
#     print(f"{i}. {names[i]}")
# last_number = len(names)
# print(f"The last name (number {last_number}) is {names[last_number]}")

# Problem(s) for program 1:
# in line 9, last_number used to index the last name is out of range
# last_number is higher than the actual last number item in the list

# Fixed code for program 1:
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names) - 1
print(f"The last name (number {last_number}) is {names[last_number]}")


# Debug program 2 - title-casing country names
# countries = ("australia", "new zeaLAND", "India")
# for i in range(len(countries)):
#     countries[i] = countries[i].title()
# print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# the tuple is used as a variable which prompts and error message
# tuples are non-mutable, so it cannot be changed

# Fixed code for program 2:
countries = ("australia", "new zeaLAND", "India")
country_list = []
for i in range(len(countries)):
    c = countries[i].title()
    country_list.append(c)  # country names should be in title-case now
    countries_titled = tuple(country_list)  # converts back into a tuple, like the exercise showed
print(countries_titled)