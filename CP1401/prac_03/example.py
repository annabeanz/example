choice = input("what kind of stake do you want? Rare; Medium; Well done:").lower()
if choice == "rare":
    print("it will take two mins")
elif choice == "medium rare":
    print("it will take 4 mins")
elif choice == "well done":
    print("it will take 6 mins")
else: print("what???")