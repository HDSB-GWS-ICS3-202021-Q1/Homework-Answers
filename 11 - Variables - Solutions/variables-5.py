#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------

p = 10000 #principal
n = 12 #compounding periods
r = 0.08 #rate of return

t = input("Please enter the number of years: ")
t = int(t)

a = p* ( 1 + (r/n))**(n*t)

print (a)



