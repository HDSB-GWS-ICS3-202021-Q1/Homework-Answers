#-----------------------------------------------------------------------------
# Name:        Homework Solution
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     18-Sept-2020
# Updated:     18-Sept-2020
#-----------------------------------------------------------------------------
userNumber = input("Please enter a number: ")
userNumber = int(userNumber)

result = 0
for i in range(1,userNumber+1,1):
    result = result + i
    print(result)
    
i =0
result = 0
while (i <= userNumber):
    result = result + i
    i = i +1

print("The sum of all numbers between 1 and "+str(userNumber)+" is "+str(result))
    

