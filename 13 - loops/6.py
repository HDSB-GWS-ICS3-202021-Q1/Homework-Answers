#-----------------------------------------------------------------------------
# Name:        Homework Solution
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     18-Feb-2021
# Updated:     18-Feb-2021
#-----------------------------------------------------------------------------


number = input("What is the number:")

number = int(number)
length = 0;

while number >= 1:
    number = number /10
    length = length + 1
    
print( f'The length is { length }')    
    
number == 0.123456


# #Another way to do this without loops (using the length command of strings)
# length = len(number)
# 
# print( f'The number is { length }')
