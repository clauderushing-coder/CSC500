# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Claude Rushing)s
"""

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = float(0.0)
        self.item_quantity = int(0)
        self.cost = self.item_price*self.item_quantity
        self.description = "none"
       
                
        
        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        self.total_cost = float(0.0)
        
        
    def add_item(self, ItemToPurchase_instance):
        if isinstance(ItemToPurchase_instance, ItemToPurchase):
            print("\nCONGRATULATIONS. YOU HAVE ENTERED A VALID ITEM TO PURCHASE.")
            self.cart_items.append(ItemToPurchase_instance)
        else:
            print("Not a valid item to purchase")
        
        ### print(self.item_name, self.item_quantity, "@",f"${self.item_price:.2f}", "=", f"${self.cost:.2f}")
        
    def remove_item(self,item_to_remove):
        print("remove item")
        
    def modify_item(self, item_to_modify):
        print("modify item")
        
    def get_num_items_in_cart(self):
        print("print numnber")
    def get_cost_of_cart(self):
        print("cost")
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            
            print(self.customer_name + "'s" + " Shopping Cart", "-", self.current_date)
            print("Number of Items:", len(self.cart_items))
            for items in self.cart_items:
                
                print(items.item_name, items.item_quantity, "@",f"${items.item_price:.2f}", "=", f"${items.cost:.2f}")
                self.total_cost = self.total_cost+items.cost
            print("Total:",f"${self.total_cost:.2f}")
            
    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            
            print(self.customer_name + "'s" + " Shopping Cart", "-", self.current_date)
            print("Item Descriptions")
            for items in self.cart_items:
                print(items.item_name +":",items.description)

        
        

def print_menu(ShoppingCart):
    
    menu = ('a - Add item to cart.\n'  # Add item
        'r - Remove item from cart.\n'  # Remove item
        'c - Change item quantity.\n'  # Change quantity
        'i - Output items\' descriptions.\n' # print descriptions
        'o - Output shopping cart.\n'
        'q - Quit.\n\n')
    print("\nPLEASE SELECT FROM THE MENU BELOW:")

    user_input = input(menu).strip().lower()

    while user_input != 'q':
        if user_input == 'a':  
            
            ValidName = False
            while ValidName == False:
    
                Item_Name = input("\nEnter the Name of the Item: ")
                print("You entered:",Item_Name)
                verify_name = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
                if verify_name == "y" or verify_name =="Y":
                    ValidName = True
                else:
                    print("\n    INCORRECT NAME ENTERED. PLEASE TRY AGAIN.")
        
            valid_price = False
            while valid_price == False:
                Item_Price_Input = (input("\nEnter the Price of the Item: "))
                try:
                    Item_Price = float(Item_Price_Input)
                    print("You have entered ", f"${Item_Price:.2f}", " as the cost for the item.")
                    valid_price = True
                    break
                except ValueError or TypeError:
                    print("Invalid format for price. Please try again, using a decimal number for the price.")

            valid_quantity = False
            while valid_quantity == False:
               Item_Quantity_Input = (input("\nEnter the Quantity of the Item: "))
               try:
                   Item_Quantity = int(Item_Quantity_Input)
                   print("You have entered ", Item_Quantity, " items.")
                   valid_quantity = True
                   break
               except ValueError or TypeError:
                   print("Invalid format for Quantity. Please try again, using an integer for the Quantity.")
        
            ValidDescription = False
            while ValidDescription == False:
    
                Item_Description = input("\nEnter the Description of the Item: ")
                print("You entered:",Item_Description)
                verify_description = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
                if verify_description == "y" or verify_description =="Y":
                    ValidDescription = True
                else:
                    print("\n    INCORRECT DESCRIPTION ENTERED. PLEASE TRY AGAIN.")
        
        
            Item = ItemToPurchase()
            Item.item_name = Item_Name
            Item.item_price = Item_Price
            Item.item_quantity = Item_Quantity
            Item.cost = Item.item_price*Item_Quantity
            Item.description = Item_Description
            ShoppingCart.add_item(Item)

        elif user_input == 'r':  
            print('Remove item\n')
        
        elif user_input == 'c':  
            print('Change Quantity.\n')

        elif user_input == 'i':  
            My_Cart.print_descriptions()
              
        elif user_input == 'o':  
            
            My_Cart.print_total()
        
           
        else:
            print('Unknown menu option')
        print("\nPLEASE SELECT FROM THE MENU BELOW:")
        user_input = input(menu).strip().lower()
      
    

ValidName = False
while ValidName == False:
    Customer_Name = input("\nEnter the Name of the Customer: ")
    print("You entered:",Customer_Name)
    verify_name = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
    if verify_name == "y" or verify_name =="Y":
        ValidName = True
    else:
      print("\n    INCORRECT NAME ENTERED. PLEASE TRY AGAIN.")
      
ValidDate = False
while ValidDate == False:
    Current_Date = input("\nEnter the Current Date: ")
    print("You entered:",Current_Date)
    verify_date = input("If this is correct, enter 'y' or 'Y'. Enter any other character to try again: ")
    if verify_date == "y" or verify_name =="Y":
        ValidDate = True
    else:
      print("\n    INCORRECT DATE ENTERED. PLEASE TRY AGAIN.")

My_Cart = ShoppingCart(Customer_Name, Current_Date)   
print_menu(My_Cart) 