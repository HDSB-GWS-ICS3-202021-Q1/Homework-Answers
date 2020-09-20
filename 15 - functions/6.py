#-----------------------------------------------------------------------------
# Name:        Homework Solution (5.py)
# Purpose:     A homework solution for ICS3
#
# Author:      Mr. Brooks
# Created:     20-Sept-2020
# Updated:     20-Sept-2020
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Name:        Homework Solution (5.py)
# Purpose:     A homework solution for ICS3
#
# Author:      Mr. Brooks
# Created:     20-Sept-2020
# Updated:     20-Sept-2020
#-----------------------------------------------------------------------------

def nFactorial(nIn):
    if nIn==1:  #Base case
        return 1;
    else:     #recursive case
        return nIn * nFactorial(nIn -1)
    

print(nFactorial(1))
print(nFactorial(2))
print(nFactorial(3))
print(nFactorial(4))
print(nFactorial(5))
print(nFactorial(10))
print(nFactorial(100))
print(nFactorial(1000))
