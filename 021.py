import time
start_time = time.time()

def d(x):
	i = 2
	y = 1

	while i < int(x/2) + 1:
		if x%i == 0:
			y += i
		i += 1
	return y

sum = i = a = b = 0
store = []

while i < 10000:
	a = d(i)
	b = d(a)
	if i == b and i != a:
		if a in store and b in store:
			sum = sum
		else:
			store.append(a)
			store.append(b)
			sum += a + b
	i += 1

print sum
print("--- %s seconds ---" % (time.time() - start_time))
