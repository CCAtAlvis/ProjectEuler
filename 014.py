import time
start_time = time.clock()

num = 999999
count = lc = ln = 0

while num > 700000:
	n = num

	while n > 1:
		if n%2 == 0:
			n = n/2
		else:
			n%2 == 1
			n = 3*n + 1

		count += 1

	if count > lc:
		lc = count
		ln = num

	count = 1
	num -= 1

print ln

print"--- %s seconds ---" % (time.clock() - start_time)
