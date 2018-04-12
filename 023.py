import time
start_time = time.time()

def isAbd(x):
	n = int(x/2) + 1
	i = 2
	sum = 1

	while i < n:
		if x%i == 0:
			sum += i
		i += 1
	return sum > x

abundant = []

f = True
check = sum = 0
i = 12

while i <= 28123:
	if isAbd(i):
		abundant.append(i)

	#print "checking %d"%(i)
	for a in abundant:
		#check = i - a
		if (i-a) in abundant:
			f = False
			#print "flase and quiting", check
			break

	if f:
		sum += i

	f = True
	i += 1

print sum
print("--- %s seconds ---" % (time.time() - start_time))
