#-----------------------------------------------------------------------------
# Name:        Homework Solution
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     18-Sept-2020
# Updated:     18-Sept-2020
#-----------------------------------------------------------------------------

for i in range(1, 10, 1):
    print("This is the "+str(i)+ " run")
    
    for j in range(1, i, 1):
        print(j , end="")
    
    print("")