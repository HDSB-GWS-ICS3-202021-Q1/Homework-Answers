#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------

dayNumber = int(input("Please enter the number of the day: "))

print("The day of the week is", end =" ")   #What the?  What's this?  Why?  Any ideas?

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
