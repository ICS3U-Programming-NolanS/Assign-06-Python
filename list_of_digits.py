#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 23th, 2022
# This program asks the user for a single whole number.
# Then write a function that accepts the number and returns a list of digits.


def list_of_digits(whole_num):

    # Empty list where you store the list of digits
    lst = []

    # Separate the whole 
    # numbers into lists of digits
    for digits in whole_num:
        lst.append(digits)

    # Print the list of digits
    print("The list of numbers is: {}".format(lst))

def main():

    try:
        # Get user's whole numb
        whole_num = int(input("Enter positive whole numbers: "))
    # Catch any erroneous/invalid input
    except Exception:
        print("You have entered an invalid input, please try again.")
    # Call the function in order to give the list of digits
    else:
        list_of_digits(whole_num)

if __name__ == "__main__":
    main()
