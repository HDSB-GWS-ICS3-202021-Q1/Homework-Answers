#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Homework Solution
#
# Author:      Mr. Brooks
# Created:     14-Sept-2020
# Updated:     14-Sept-2020
#-----------------------------------------------------------------------------
'''You go on a wonderful holiday leaving on day number 3 (a Wednesday).
You return home after 137 sleeps.
Write a general version of the program which asks for:
    the starting day number, and
    the length of your stay, and
    
it will tell you the name of day of the week you will return on.
'''

dayNumber = 3
sleepsNumber = 1

print("Weeks away: "+ str( sleepsNumber//7))  #Not necessary, but to help show the logic
print("Days away: "+ str(sleepsNumber % 7))   #Not necessary, but to help show the logic

dayNumber = dayNumber + sleepsNumber % 7

# if dayNumber >= 7:                          #Why is this section necessary?
#     dayNumber = dayNumber - 7

print("You return from your vacation on ", end ="")   #What the?  What's this?  Why?  Any ideas?

if dayNumber == 0:
    print("Sunday");
elif dayNumber == 1:
    print("Monday")
elif dayNumber == 2:
    print("Tuesday")
elif dayNumber == 3:
    print("Wednesday")
elif dayNumber == 4:
    print("Thursday")
elif dayNumber == 5:
    print("Friday")
elif dayNumber == 6:
    print("Saturday")
else: #This part is not required, but it shows simple error checking
    print("Tuna Fish")