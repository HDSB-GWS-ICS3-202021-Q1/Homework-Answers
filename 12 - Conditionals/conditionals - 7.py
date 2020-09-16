#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
'''
Extend the above program so that the sides can be given to the function in any order.
'''

#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
'''
Write a program is_rightangled.py which,
given the length of three sides of a triangle,
will determine whether the triangle is right-angled.
Assume that the third argument given is always the longest side.
It will return True if the triangle is right-angled, or False otherwise.


Hint: Floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as:
if  abs(x-y) < 0.000001:    # If x is approximately equal to y    
...
'''
#Get the data
sideA = float(input("Please enter the length of the side of a triangle: "))
sideB = float(input("Please enter the length of another side of a triangle: "))
sideC = float(input("Please enter the length of the final side of a triangle: "))


#find out which side is the longest

if sideA > sideC: #if sideA is bigger than sideC, swap the lengths to make C the longest
    tempSide = sideC
    sideC = sideA
    sideA = tempSide

if sideB > sideC: #if sideB is bigger than sideC, swap the lengths to make C the longest
    tempSide = sideC
    sideC = sideB
    sideB = tempSide
 
#sideC variable now stores the longest side of the triangle.

#Let's test it out:
print("The side lengths are", sideA, sideB, sideC)


calulatedSideC = ( sideA*sideA + sideB*sideB)**0.5

if  abs(sideC-calulatedSideC) < 0.000001:    # If x is approximately equal to y
    print("This triangle is a right angled triangle")
else:
    print("This triangle is NOT a right angled triangle")
    

