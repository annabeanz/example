
"""
get birth_month
while birth_month < 1 or birth_month > 12
    display error message
    get birth_month
for count from 1 to birth_month
    display count
if birth_month < 6
    display "you are born in the first half of the year"
else
    display "you are born in the seccond half of the year"
"""

MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12
month_born = int(input(f"What month were you born in? ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while month_born > MAXIMUM_MONTH or month_born < MINIMUM_MONTH:
    print("Please enter a valid month")
    month_born
for counting in range (1,month_born + 1):
    print(counting, end=" ")
print()
if month_born < 6:
    print("You are born in the first half of the year")
else:
    print("You are born in the second half of the year")