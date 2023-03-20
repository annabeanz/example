"""CP1401 - Practical 10 - Debugging.
Explain the problems (not the solution, not the style issues):
1) money + result seem to be in different types, result should not be a none-type
2) Amount entered does not use decimal values, thus cannot input $0.5 even if it's in my balance

Describe your debugging process:
1) Removed unneeded indentation so that result is returned at the end of the function - line 61
2) in get_valid_amount int() is replaced with float() - line 25, 38, 44
(stylistic) starting amount now stored in a constant STARTING_AMOUNT, so it can be changed - line 21, 25
(stylistic) print("Invalid choice") was over-indented, removed indentation - line 50

Fix the code in-place below
"""
import random

VALID_CHOICES = 'AC'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 50
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 80
STARTING_AMOUNT = 100


def main():
    money = float(STARTING_AMOUNT)
    print("Welcome to the futility of gambling!")
    print(f"You start with a balance of ${STARTING_AMOUNT}.")
    while money > 0:
        result = play(money)
        money = money + result
        print(f"Your new balance is ${money:.2f}")
    print("You lost :)")


def get_valid_amount(balance, amount):
    while amount < 0 or amount > balance:
        print("Invalid amount")
        amount = float(input("Enter amount to play: "))
    return amount


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount = float(input("Enter amount to play: "))
    amount_to_risk = get_valid_amount(balance, amount)
    choice = 'x'
    while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
            print("Invalid choice")
    risk_chance = random.randint(0, 101)
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = (amount_to_risk * (CONSERVATIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = (amount_to_risk * (AGGRESSIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
    return result


main()
