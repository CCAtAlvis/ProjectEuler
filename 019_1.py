#this program does not use make day or that kind of function although thats easer but thats not fun
#and is being built... check the easer program for answer
import time
start_time = time.time()

#making a switch in python
def switch(x):
	return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found
#of no use here use if..elif instead
#no not even that array.. oops list it is for win

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 1

days = months[month]
day = 1

monthday = 1
weekday = 1
yearday = 1

year = 1901
#0: false
#1: true
leap = 0

count = 0

while year <= 2000:
	if (year%4 == 0 and (year%100 != 0 or year%400 == 0)):
		leap = 1

	if 

	#if (leap == 1):
	#	print "hello"


	year += 1

print("--- %s seconds ---" % (time.time() - start_time))
