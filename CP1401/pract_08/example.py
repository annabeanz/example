"""
places = empty list
get place
while place is not empty
    add place to places
    get place
for place in places
    print place
"""

places = []
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ")
if len(places) < 1:
    print("I went nowhere")
else:
    print("On my holiday, I went to: ")
    for place in places:
        longest_place = ""
        if len(place) > len(longest_place):
            longest_place = place
        print(place)
    print("Your longest place is", longest_place)
