import time
start_time = time.time()

num = 3
counter = sum = 2
key = temp = 0

while num < 2000000:
	temp = num
	while counter * counter <= num:
		if num % counter == 0:
			num = num/counter
			key = 1
			break
		else:
			counter += 1

	if key == 0 :
		sum += temp
		print temp

	num = temp + 2
	counter = 2
	key = 0

print sum

print("--- %s seconds ---" % (time.time() - start_time))