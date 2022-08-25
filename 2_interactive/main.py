from random import randint

while True:
    try:
        min = int(input("Enter a number: "))
        max = int(input("Enter another number: "))

        if min >= max: continue

        print(f"Random number: {randint(min, max)}\n", )
    except ValueError:
        continue
