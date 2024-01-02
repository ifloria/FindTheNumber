import random
import os

os.system('cls')

def find_the_number():
    number_list = list(range(0, 101))
    x = random.choice(number_list)

    y = int(input("Enter a number 1-100: "))

    if x == y:
        print(f"yea! Number: {x}")
    else:
        print(f"nope! Number: {x}")

    while True:
        response = input("Do You Want To Play Again? (yes or no): ").lower()
        if response == "yes":
            find_the_number()
        elif response == "no":
            break

find_the_number()
