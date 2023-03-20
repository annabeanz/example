#2. Parity
"""
function main()
    number = ("give a number: ")
    printed_parity(number)
    if is_odd(number)
        print odd
    else
        print even

    parity_returned = get_parity(number)
    print parity_returned
    if is_odd(number)
        print odd
    else
        print even

function printed_parity(number)
    parity = number % 2
    print parity

function get_parity(number)
    parity = number % 2
    return parity

function is_odd(number)
    return number % 2 == 1
"""
def main():
    number = (int(input("Give a number: ")))
    print(f"The parity of {number} is", end=" ") # function "printed_parity" cannot be printed together
    printed_parity(number) #So it is called separately, printing on the same line
    if is_odd(number):
        print(" it is odd")
    else:
        print(" it is even")

    parity_returned = get_parity(number)
    print(f"The parity of {number} is {parity_returned}", end=" ")
    #this statement uses the return function to print it all together
    if is_odd(number):
        print("it is odd")
    else:
        print("it is even")

def printed_parity(prompt): #uses the print function
    parity = prompt % 2
    print(parity, end="")

def get_parity(prompt): #uses the return function
    parity = prompt % 2
    return parity

def is_odd(number):
    return number % 2 == 1 #returns True or False

main()
