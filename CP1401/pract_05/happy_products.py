# All Together Now
"""
display MENU
get choice
while choice !=  quit and choice != q
    if choice == i or if choice == instructions
        display instructions
    else if choice == c or choice == calculate
        get number_of_products
        while number_of_products < 0
            display ERROR_MESSAGE
            get number_of_products
        get price
        while price < 0
            display ERROR_MESSAGE
            get price
        total = number_of_products * price
        if number_of_products <= 5
            display total
        else
            display total * 0.9
    else
        display ERROR_MESSAGE
    display MENU
    get choice
display farewell
"""

INSTRUCTIONS = """Enter the number of products you want to buy and your chosen price. 
If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!"""
ERROR_MESSAGE = "Invalid choice"
MENU = """Menu:
(I)nstructions
(C)alculate
(Q)uit"""

print(MENU)
choice = input("Choice: ").lower()
while choice != "quit" and choice != "q":
    if choice == "i" or choice == "instructions":
        print(INSTRUCTIONS)
    elif choice == "c" or choice == "calculate":
        number_of_products = int(input("Number of products: "))
        while number_of_products < 0:
            print(ERROR_MESSAGE)
            number_of_products = int(input("Number of products: "))
        price = float(input("Price: $"))
        while price < 0:
            print(ERROR_MESSAGE)
            price = float(input("Price: $"))
        total = number_of_products * price
        if number_of_products <= 5:
            total = total
        else:
            total = total * 0.9
        print(f"{number_of_products} x ${price} will total to: ${total:,.2f}")
    else:
        print(ERROR_MESSAGE)
    print(MENU)
    choice = input("Choice: ").lower()
print("Farewell")
