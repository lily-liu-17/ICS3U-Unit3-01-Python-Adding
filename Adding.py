#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program can add 2 numbers together
#   numbers are given by user


def main():
    # input
    first_number = int(input("Enter the first number to add (integer) : "))
    second_number = int(input("Enter the second number to add (integer) : "))

    # process
    total = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, total))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
