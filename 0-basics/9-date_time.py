
import time
import calendar
import datetime  # Checkout datetime module
from datetime import datetime

# A Tick
# Time intervals are floating-point numbers in unit of seconds
# Ticks are calculated from epoch
# Limitation : Dates before 1970 and future dates at somepoint after 2038
print(time.time())

# TimeTuple
# The structure struct_time
# Index	Attributes	Values
# 0	tm_year	2008
# 1	tm_mon	1 to 12
# 2	tm_mday	1 to 31
# 3	tm_hour	0 to 23
# 4	tm_min	0 to 59
# 5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
# 6	tm_wday	0 to 6 (0 is Monday) Day of the week
# 7	tm_yday	1 to 366 (Julian day) Day of the year
# 8	tm_isdst	-1, 0, 1, -1 means library determines DST Daylight Savings

# Convert an epoch based float to struct_time using time.localtime()
myTimeTuple = time.localtime(time.time())
print(myTimeTuple)
print(type(myTimeTuple))

# Converting a time-tuple to epoch
myTimeEpoch = time.mktime(myTimeTuple)
print('myTimeEpoch is ', myTimeEpoch)

# Simplest way to format the struct_time to readable format. time.asctime(time-tuple)
myTime = time.asctime(myTimeTuple)
print(myTime)
print(type(myTime))

print('Sleeping for 2 seconds')
time.sleep(2)
myCurCal = calendar.month(2018, 6)
print(myCurCal)

print(calendar.isleap(2000))
print(calendar.leapdays(2000, 2010))

# Explore other Built In functions in time and calendar modules
print(dir(datetime))

now = datetime.now()
then = datetime(2010,7,31)
delta = now - then

print(type(delta))
print("No of days passed since %s are %d" % (then.strftime("%x"), delta.days))
print("Time now is : ", now.strftime("%Y-%m-%d-%H-%M-%S-%f"))