# -*- coding: utf-8 -*-

# Spyder Editor


class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = float(0.0)
        self.item_quantity = int(0)
        self.cost = float(0.0)
        
    def print_item_cost(self):
        line_width = 50
        
        print(self.item_name, self.item_quantity, "@",f"${self.item_price:.2f}", "=", f"${self.cost:.2f}")
        
ValidName = False
while ValidName == False:
    
    Item_One_Name = input("\nEnter the Name of the First Item: ")
    print("You entered:",Item_One_Name)
    verify_name = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
    if verify_name == "y" or verify_name =="Y":
        ValidName = True
    else:
        print("\n    INCORRECT NAME ENTERED. PLEASE TRY AGAIN.")
        


valid_price = False
while valid_price == False:
    Item_One_Price_Input = (input("\nEnter the Price of the First Item: "))
    try:
        Item_One_Price = float(Item_One_Price_Input)
        print("You have entered ", f"${Item_One_Price:.2f}", " as the cost for item one.\n")
        valid_price = True
        break
    except ValueError or TypeError:
        print("Invalid format for price. Please try again, using a decimal number for the price.")

valid_quantity = False
while valid_quantity == False:
    Item_One_Quantity_Input = (input("\nEnter the Quantity of the First Item: "))
    try:
        Item_One_Quantity = int(Item_One_Quantity_Input)
        print("You have entered ", Item_One_Quantity, " items.\n")
        valid_quantity = True
        break
    except ValueError or TypeError:
        print("Invalid format for Quantity. Please try again, using an integer for the Quantity.")


Item_One = ItemToPurchase()
Item_One.item_name = Item_One_Name
Item_One.item_price = Item_One_Price
Item_One.item_quantity = Item_One_Quantity
Item_One.cost = Item_One.item_price*Item_One_Quantity


ValidName = False
while ValidName == False:
    
    Item_Two_Name = input("\nEnter the Name of the Second Item: ")
    print("You entered:",Item_Two_Name)
    verify_name = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
    if verify_name == "y" or verify_name =="Y":
        ValidName = True
    else:
         print("\n    INCORRECT NAME ENTERED. PLEASE TRY AGAIN.")
        
valid_price = False
while valid_price == False:
    Item_Two_Price_Input = (input("\nEnter the Price of the Second Item: "))
    try:
        Item_Two_Price = float(Item_Two_Price_Input)
        print("Your have entered ", f"{Item_Two_Price:.2f}", " as the cost for item two.\n")
        valid_price = True
        break
    except ValueError or TypeError:
        print("Invalid format for price. Please try again, using a decimal number for the price.")

valid_quantity = False
while valid_quantity == False:
    Item_Two_Quantity_Input = (input("\nEnter the Quantity of the Second Item: "))
    try:
        Item_Two_Quantity = int(Item_Two_Quantity_Input)
        print("Your have entered ", Item_Two_Quantity, " items.\n")
        valid_quantity = True
        break
    except ValueError or TypeError:
        print("Invalid format for Quantity. Please try again, using an integer for the Quantity.")
        
Item_Two = ItemToPurchase()
Item_Two.item_name = Item_Two_Name
Item_Two.item_price = Item_Two_Price
Item_Two.item_quantity = Item_Two_Quantity
Item_Two.cost = Item_Two.item_price*Item_Two_Quantity
print("\nTOTAL COST")
Item_One.print_item_cost()
Item_Two.print_item_cost()
print("Total: ",f"${Item_One.cost+Item_Two.cost:.2f}")



