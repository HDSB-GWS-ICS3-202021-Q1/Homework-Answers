#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
'''
Write a program find_hypot.py which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)
'''
sideA = float(input("Please enter the length of side A of a triangle: "))
sideB = float(input("Please enter the length of side B of a triangle: "))

sideC = ( sideA*sideA + sideB*sideB)**0.5

print("The length of the hypotenuse is: ", str(sideC))