# -*- coding: utf-8 -*-
"""
     
Created on Aug 23 2025

@author: Claude Rushing
"""
### This program calculates the total cost of a meal including the charge, 18% tip and 7% sales tax

            
def validate_dollar_input(input_str):

### Validates that the input is a float with only two decimal places.

    try:
        # validate that the float is a valid number
        float_check = float(input_str)

        # Check if the input contains a decimal point
        if '.' not in input_str:
            return False

        # Split the string at the decimal point
        split_parts = input_str.split('.')
        decimal_part = split_parts[1]

        # Check if there are only 2 decimal places
        if len(decimal_part) == 2:
            return True
        else:
            return False
    except ValueError:
        return False  # Input is not a valid float
    
### The main program starts here

valid_input = False
while valid_input == False:
    user_input = input("\nPlease enter the charge for the food as a dollar amount with 2 decimal places: ")

    if validate_dollar_input(user_input):
        
        food_charge = float(user_input)
        tip_amount = float(food_charge*.18)
        sales_tax = float(food_charge*.07)
        total_amount = food_charge + tip_amount + sales_tax
        print(f"\nThe Total Amount of the Bill:  ${total_amount:.2f}")
        print(f"\nFood Charge: ${food_charge:.2f}")
        print(f"\nTip Amount: ${tip_amount:.2f}")
        print(f"\nSales Tax: ${sales_tax:.2f}")
        print("\nThanks for Dining with us!")
        valid_input = True
    else:
        print(f"'{user_input}' is not a valid dollar amount with two decimal places.")
        print("PLEASE TRY AGAIN")            
            


