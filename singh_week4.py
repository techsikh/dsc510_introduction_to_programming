"""
===========================================
Title: Assignment 4.1
Author: Jujahar Singh
Date: 18 September 2025
Description: DSC 510 Week 2 - This program calculates the total cost a
             Company would pay to install a provided length of fiber
             optic cable.
Change#: 1
Change(s) Made: Selecting cost of cable bases on the ordered length.
                Added Exception Handling for Invalid User Input
Date of Change: 25 September 2025
Author: Jujahar Singh
Change#: 2
Change(s) Made: Grouping logic within functions and controlling the execution
                from main method
Date of Change: 02 October 2025
Author: Jujahar Singh
===========================================
"""

def get_company_name():
    """asks user for company name and returns it"""
    company_name_from_user = input("Please enter your company name: ")

    # Initialize variable to check if user actually entered something
    company_name = None

    # Referred below link for the retry logic inspiration
    # https://stackoverflow.com/a/34789951
    while (company_name is None) or (company_name.strip() == ""):
        company_name = company_name_from_user
        if company_name.strip() == "":
            company_name_from_user = input("Please enter a valid name: ")
    return company_name


def get_cable_length():
    """asks user for cable length and returns it"""
    # Get the cable length from the user
    cable_length_string = input("Enter how much cable you need in feet: ")
    cable_length = 0

    # Check if user entered a valid number otherwise show an error message
    try:
        # Convert the string length provided by the user to a number
        cable_length = float(cable_length_string)
    except ValueError:
        print(f"Error: please enter a numeric value for the cable length.")
    return cable_length


def calculate_cost(cable_feet, price_per_foot):
    """Calculates the total installation cost of cable based on the length"""
    return cable_feet * price_per_foot


def print_receipt(company_name, cable_length, installation_cost):
    """Prints the receipt for the given cable length and installation cost"""
    print("------------------------------")
    print("Installation Receipt")
    print("------------------------------")
    print(f"Company:       {company_name}")
    print(f"Cable Length:  {cable_length}")
    print(f"Total Cost:    ${installation_cost:.2f}")
    print("------------------------------")
    print("Thank you for your business!")


def main():
    # Welcome the customer
    print("Welcome. Let's calculate fiber optic cable installation cost.")

    # get company name from the user
    company_name = get_company_name()

    # get cable length from the user
    cable_length = get_cable_length()

    # Initialize variable which will store the installation cost
    installation_cost = 0

    # Calculate the installation cost by multiplying the per-foot cost,
    # which is based on the length of the cable ordered, with the total
    # cable length
    if cable_length > 500:
        installation_cost = calculate_cost(cable_length, 0.55)
    elif cable_length > 250:
        installation_cost = calculate_cost(cable_length, 0.75)
    elif cable_length > 100:
        installation_cost = calculate_cost(cable_length, 0.85)
    else:
        installation_cost = calculate_cost(cable_length, 0.95)
    print_receipt(company_name, cable_length, installation_cost)


if __name__ == "__main__":
    main()



