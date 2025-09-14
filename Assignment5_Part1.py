# -*- coding: utf-8 -*-

# Spyder Editor


rainfall = 0.0
total_rainfall = 0.00
total_months = int(0)
average_rainfall = 0.00

valid_years = False
while valid_years == False:
    years_input = (input('\nEnter the number of years to process: \n'))
    try:
        years = int(years_input)
        print("You have entered ", years, " years.\n")
        valid_years = True
        break
    except ValueError or TypeError:
        print("Invalid format for Number of Years. Please try again, using an integer for the Number of years.")
    

months = ['JANUARY: ', 'FEBRUARY: ', 'MARCH: ', 'APRIL: ','MAY: ', 'JUNE: ', 'JULY: ', 'AUGUST: ', 'SEPTEMBER: ', 'OCTOBER: ', 'NOVEMBER: ', 'DECEMBER: ']


for i in range(years):
    for j in months:
       
        total_months = total_months + 1
        valid_rainfall = False
        while valid_rainfall == False:
            rainfall_input = input('Enter the number of inches of rainfall in {} ' .format(j),)
            try:
                rainfall = float(rainfall_input)
              ###  print("You have entered ", f"{rainfall:.2f}")
                total_rainfall = total_rainfall + rainfall
                valid_rainfall = True
                break
            except ValueError or TypeError:
                print("Invalid format for rainfall. Please try again, using a decimal number for the amount of rainfall in inches.")
          

       
average_rainfall = total_rainfall/total_months
   
print('\nThe Number of Months = ', total_months)
print('\nTotal Rainfall = ', f"{total_rainfall:.2f}", ' inches')
print('\nAverage Rainfall = ',f"{average_rainfall:.2f}","inches")




