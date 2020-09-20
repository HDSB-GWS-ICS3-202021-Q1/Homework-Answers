#-----------------------------------------------------------------------------
# Name:        Homework Solution (1.py)
# Purpose:     A homework solution for ICS3
#
# Author:      Mr. Brooks
# Created:     20-Sept-2020
# Updated:     20-Sept-2020
#-----------------------------------------------------------------------------


def whatDayIsIt(dayNumberIn):
    '''Return the text for the day given it's numeric value '''
    
    if dayNumber == 0:
        return("Sunday");
    elif dayNumber == 1:
        return("Monday")
    elif dayNumber == 2:
        return("Tuesday")
    elif dayNumber == 3:
        return("Wednesday")
    elif dayNumber == 4:
        return("Thursday")
    elif dayNumber == 5:
        return("Friday")
    elif dayNumber == 6:
        return("Saturday")
    else: #This part is not required, but it shows simple error checking
        return("Error")



#Get user input
dayNumber = int(input("Please enter the number of the day: "))

#Call the function AND print results at the same time
print("The day of the week is " + whatDayIsIt(dayNumber))   
