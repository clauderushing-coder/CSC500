# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Claude Rushing)s
"""

room_number_dict = {"CSC101": "3004","CSC102": "4501","CSC103": "6755","NET110": "1244","COM241": "1411" }
instructor_dict = {"CSC101": "Haynes","CSC102": "Alvarado","CSC103": "Rich","NET110": "Burke","COM241": "Lee" }
time_dict = {"CSC101": "8:00 a.m.","CSC102": "9:00 a.m.","CSC103": "10:00 a.m.","NET110": "11:00 a.m.","COM241": "1:00 p.m." }

valid_input = False

menu_prompt = "\nSelect an Option from the Menu Below:\n\n \
    1 - Get Room Number.\n \
    2 - Get Instructor Name.\n \
    3 - Get Meeting Time.\n \
    4 - Get All Course Information \n \
    5 - QUIT\n"

while valid_input == False:
    
      
    user_input = input(menu_prompt)

    if user_input == "1":
        valid_number = False
        while valid_number == False:
            
            course_number = input("Please Enter the Course Number\n")
            if course_number in room_number_dict:
                
                print("The ROOM NUMBER for ", course_number, " is: ",room_number_dict[course_number])
                valid_number = True
            else:
                print("INVALD COURSE NUMBER. PLEASE TRY AGAIN!\n")
            
    elif user_input == "2":
        valid_number = False
        while valid_number == False:
            
            course_number = input("Please Enter the Course Number\n")
            if course_number in instructor_dict:
                
                print("The INSTRUCTOR for ", course_number, " is: ",instructor_dict[course_number])
                valid_number = True
            else:
                print("INVALD COURSE NUMBER. PLEASE TRY AGAIN!\n")        
       
    elif user_input == "3":
        valid_number = False
        while valid_number == False:
            
            course_number = input("Please Enter the Course Number\n")
            if course_number in time_dict:
                
                print("The TIME for ", course_number, " is: ",time_dict[course_number])
                valid_number = True
            else:
                print("INVALD COURSE NUMBER. PLEASE TRY AGAIN!\n")
                
    elif user_input == "4":
        valid_number = False
        while valid_number == False:
            
            course_number = input("Please Enter the Course Number\n")
            if (course_number in time_dict) and (course_number in instructor_dict) and (course_number in room_number_dict):
                print("The ROOM NUMBER for ", course_number, " is: ",room_number_dict[course_number])
                print("The INSTRUCTOR for ", course_number, " is: ",instructor_dict[course_number])
                print("The TIME for ", course_number, " is: ",time_dict[course_number])
                valid_number = True
            else:
                print("INVALD COURSE NUMBER. PLEASE TRY AGAIN!\n") 
    elif user_input == "5":
        print("GOODBYE!!")
        break
    
    else:
        print("\nINVALID INPUT. PLEASE SELECT FROM THE MENU BELOW:\n" )