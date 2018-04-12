#this program uses make day or that kind of function although thats easer but thats not fun
#and is built... check this for answer
#you could also go over to the 019_1.py for a more fun algorithm
import time
start_time = time.time()
import datetime

year = 1901
month = 1
date = 0

c = 0

while year <= 2000:
	while month <= 12:
		date = datetime.date(year, month, 1).weekday()
		c = c + 1 if date == 6 else c
		month += 1
	month = 1
	year += 1

print c
print("--- %s seconds ---" % (time.time() - start_time))
