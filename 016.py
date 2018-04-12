import time
start_time = time.clock()

num = 2**1000
num = str(num)
sum = i = 0

for i in range(len(num)):
	sum += int(num[i])

print sum

print"--- %s seconds ---" % (time.clock() - start_time)
