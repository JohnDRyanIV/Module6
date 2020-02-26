# Program: string_functions
# Author: John Ryan
# Last modified: 2/26/2020

# This program takes a string and number (n) input by the user and outputs that string
# n number of times


def multiply_string(m, n):
    """
    returns string m repeating n times
    :param m: represents message to be repeated
    :param n: represents amount of times message will repeat
    """
    r = ""
    for i in range(0, n):
        r = r + m
    return r


if __name__ == '__main__':
    try:
        message = str(input("Enter a message: "))
        repeat = int(input("Enter the number of times you want that message to repeat: "))
    except ValueError as err:
        print("Invalid input. Run again.")
    else:
        message = multiply_string(message, repeat)
    print(message)