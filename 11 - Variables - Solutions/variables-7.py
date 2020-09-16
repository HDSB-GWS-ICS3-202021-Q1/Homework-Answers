#-----------------------------------------------------------------------------
# Name:        New File Generator (newFile.py)
# Purpose:     Generates a new file for use in the ICS3U course
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
'''
You look at the clock and it is exactly 2pm.
You set an alarm to go off in 51 hours.
At what time does the alarm go off?

(Hint: you could count on your fingers, but this is not what we’re after.
If you are tempted to count on your fingers, change the 51 to 5100.)
(Hint 2: Use 24 hour clocks to make it easier)
'''

currentTime = 12+2  #Time in 24 hr time

hoursUntilAlarm = 51

alarmTime = currentTime + 51%24

print (" The alarm will go off at ", alarmTime-12)