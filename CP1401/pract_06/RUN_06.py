def main():
    age = get_age()

    print(f"At {age}, you are half-way to {age * 2}")


def get_age():
    x = int(input("Age: "))

    return x


main()