# -*- coding: utf-8 -*-
"""
     
Created on Aug 23 2025

@author: Claude Rushing
"""
""" This program determines and displays the number of points awarded to the user 
based on the number of books purchased """

    
### The main program starts here

valid_number_of_books = False
while valid_number_of_books == False:
    books_purchased_input = (input('\nEnter the number of books that you purchased: \n'))
    try:
        books_purchased = int(books_purchased_input)
        if books_purchased >= 0:
            print("You have entered ", books_purchased, " books.\n")
            valid_number_of_books = True
            break
        else:
            print("Input must be greater than or equal to zero. Please try again.")
           
    except ValueError or TypeError:
        print("Invalid format for Number of Books. Please try again, using an integer for the Number of books.")

if books_purchased <= 1:
    print("You earned 0 points! Are you illiterate?")
elif books_purchased <= 3:
    print("You earned 5 points! Let's do better next month!")
elif books_purchased <= 5:
    print("You earned 15 points! Your amount of reading is about Average")
elif books_purchased <= 7:
    print("You earned 30 points. That's a lot of books!")
else:
    print("WOW! You earned 60 points. You might make the Guiness record book!")
