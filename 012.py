import time
import math
start_time = time.clock()

num = key = 0
factors = divisor = 1
n = 10000

while 1>0:
	num = n*(n+1)/2
	
	while divisor <= int(math.ceil(math.sqrt(num)))+1:
		if num%divisor == 0:
			factors += 2

		if divisor*divisor == num:
			factors -=1
		
		divisor += 1
		if factors > 500:
			key = 1
			break
	
	if key > 0:
		break
		
	n += 1
	divisor = factors = 1

print num

print("--- %s seconds ---" % (time.clock() - start_time))
