# -*- coding: utf-8 -*-
"""
     
Created on Aug 28 2025

@author: Claude Rushing
"""
### This program asks the user to input a specific time, followed by the number of hours to wait for an alarm to go off. 
### The program will display the time that the alarm will go off, using the 24 hour clock.

from datetime import datetime, timedelta, time
            
def get_time_input(prompt="Enter a time using the 24-hour clock format (HH:MM)): ", time_format="%H:%M"):
   
###    Prompts the user for a time and validates that it is formatted correctly.

    while True:
        
        input_time = input(prompt)
        try:
            # validate if the input is a valid datetime object
            valid_time = datetime.strptime(input_time, time_format).time()
            return valid_time
        
        except ValueError:
            print("\nThat is not a valid time. Please try again using the correct format:", time_format)
            
### Main Program starts here

print("\n")
user_input = get_time_input()
print("\nThe time entered is:", user_input.strftime("%H:%M"))
print("\nNow enter the number of HOURS and MINUTES before the alarm goes off:\n")

### Prompts for the number of hours to wait and validate that a valid integer is entered

valid_hours = False
while valid_hours == False:
    hours_to_wait_input = input("STEP 1: Enter the number of HOURS to wait for the alarm as an integer: ")
    try:
        hours_to_wait = int(hours_to_wait_input)
        print("Your have entered ", hours_to_wait, " hours to wait for the alarm.\n")
        valid_hours = True
        break
    except ValueError or TypeError:
        print("Invalid format for number of hours. Please try again")
        
### Prompts for the number of minutes to wait and validates that an integer between 0 and 60 is entered
        
valid_minutes = False
while valid_minutes == False:
    minutes_to_wait_input = input("STEP 2: Enter the number of additional MINUTES to wait for the alarm as an integer between 0 and 60: ")
    try:
        minutes_to_wait = int(minutes_to_wait_input)
        if minutes_to_wait >= 0 and minutes_to_wait < 61:
            print("You have entered ", minutes_to_wait, "additional minutes to wait for the alarm")
            valid_minutes = True
        else:
            print("Sorry, the number of minutes must be between 0 and 60. Please try again!\n")
    except ValueError or TypeError:
        print("Invalid format for number of minutes. Please try again\n")
        
### Display the number of hours and minutes to wait
        
print("\nYou have entered ",hours_to_wait, " hours and ", minutes_to_wait, " minutes to wait for the alarm")
    
### Calculate the time that the alarm will go off


user_time = datetime(month=8,day=29,year=2025,hour=user_input.hour, minute=user_input.minute)
delta_time = timedelta(hours=hours_to_wait%24, minutes=minutes_to_wait)

print("\nTime entered by User: ", user_time.strftime("%H:%M"))
print("\nTime to Wait for Alarm: ", hours_to_wait, " hours and ", minutes_to_wait, " minutes")



alarm_time = user_time + delta_time

 ## Print the alarm time
print("\n     THE ALARM WILL GO OFF AT: ", alarm_time.strftime("%H:%M"))
 
    
  

       
            


