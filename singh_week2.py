"""
===========================================
Title: Assignment 2.1
Author: Jujahar Singh
Date: 18 September 2025
Description: DSC 510 Week 2 - This program calculates the total cost
             of installing fiber optic cable.
===========================================
"""
# Define Constant for the per foot cost
CABLE_COST_PER_FOOT = 0.95

# Welcome the customer
print("Welcome. Let's calculate fiber optic cable installation cost.")

# Get company name from the user
company_name = input("Please enter your company's name: ")

# Get the cable length from the user
cable_length_string = input("Enter how much fiber optical you need in feet: ")
cable_length = None
try:
    # Convert the string length provided by the user to a floating number
    cable_length = float(cable_length_string)
except ValueError:
    print(f"Error: please enter a numeric value for the cable length.")

# Calculate the installation cost by multiplying the per-foot cost
# by the total cable length
installation_cost = CABLE_COST_PER_FOOT * cable_length

# Referred StackOverflow for the following multi-line print Syntax
# https://stackoverflow.com/a/55168030
print(f"""
------------------------------
     Installation Receipt     
------------------------------
Company:       {company_name}
Cable Length:  {cable_length}
Total Cost:    ${installation_cost:.2f}
------------------------------
Thank you for your business!
""")



