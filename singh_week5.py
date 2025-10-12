"""
===========================================
Title: Assignment 5.1
Author: Jujahar Singh
Date: 10 October 2025
Description: DSC 510 Week 5 - This programs does addition, substraction,
             division, multiplication with 2 numbers and also calculates
             average of numbers. User selects how many numbers they
             want to average out.
===========================================
"""


def perform_calculation(operator):
    """applies the passed operator on 2 numbers which user provides"""
    first_number = get_numeric_input(1)
    second_number = get_numeric_input(2)
    print(f"You entered {first_number} and {second_number}")
    result = None

    # Since we are validating the operator beforehand we will not get
    # any other value, just check for operator and do the operation
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number
    return result


def get_numeric_input(input_counter):
    """get numeric input from user and retry until it is valid"""
    number_string = input(f"Enter number {input_counter}: ")

    # Initialize variable to store result
    number = None

    # Referred below link for the retry logic inspiration
    # https://stackoverflow.com/a/34789951
    while (number is None) or (number_string.strip() == ""):
        try:
            # Convert the string length provided by the user to a float
            number = float(number_string)
        except ValueError:
            number_string = input("Error: please enter a number: ")
    return number


def get_specific_input(valid_values, input_message):
    """force user to enter one of the valid values and return"""
    # Initialize variable to store user input
    user_input = None

    # keep asking user for inout until the enter one of the valid values
    while (user_input is None) or (user_input not in valid_values):
        user_input = input(input_message)
    return user_input


def calculate_average():
    """Ask the user how many numbers they wish to input
    and calculate average.
    """
    # Get the count of numbers from user
    number_count_str = input("Enter how many numbers you wish to average: ")
    number_count = 0

    # Referred below link for the retry logic inspiration
    # https://stackoverflow.com/a/34789951
    while (number_count == 0) or (number_count_str.strip() == ""):
        try:
            # Convert the string length provided by the user to a number
            number_count = int(number_count_str)
        except ValueError:
            number_count_str = input("Error: please enter a number: ")

    # Initialize variable to store the user inputs
    numbers_list = []

    # Initialize variable to store the sum of user entered numbers
    sum_of_numbers = 0

    # ask user for input until number_count number of times
    # also add each provided number to the total sum
    # Referred https://www.w3schools.com/python/ref_func_range.asp
    for counter in range(number_count):
        numeric_input = get_numeric_input(counter + 1)
        numbers_list.append(numeric_input)
        sum_of_numbers = sum_of_numbers + numeric_input

    # calculate average
    average = sum_of_numbers / number_count
    print(f"You entered {numbers_list}.")
    return average


def main():
    # Keep asking user for input and do either the add, subtract,
    # multiply, divide or average. User can also exit by entering -1
    while True:
        print("What would you like to do?")
        print("To calculate average, type 'average'")
        print("OR")
        print("To add, subtract, divide or multiply type 'calculation'")
        print("OR")
        user_selection = input("Enter -1 to exit: ")

        if user_selection == "average":
            average = calculate_average()
            print(f"The average of the entered numbers is {average:.2f}")
            print("==============================")
        elif user_selection == "calculation":
            message = ("Enter '+' for addition, '-' for subtraction, "
                       "'*' for multiplication or '/' for division: ")
            operator = get_specific_input(["+", "-", "*", "/"], message)
            result = perform_calculation(operator)
            print(f"Result of the {operator} operation is {result:.2f}")
            print("==============================")
        elif user_selection == "-1":
            print("Thank you")
            break
        else:
            print("Error: please enter a valid option.")


if __name__ == "__main__":
    main()
