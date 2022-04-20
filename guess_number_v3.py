#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program allows user to guess number


import random


def main():
    # I check if the user guessed correctly
    chosen_number = random.randint(0, 9)

    while True:
        # input
        string_guess = input("Guess a number between 0-9: ")

        # process&output
        try:
            int_guess = int(string_guess)
            if chosen_number == int_guess:
                print("You got it!")
                break
            elif chosen_number > int_guess:
                print("Too low!")
            else:
                print("Too high!")
        except Exception:
            print("Please enter an integer!")
    print("\nDone.")


if __name__ == "__main__":
    main()
