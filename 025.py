import time
start_time = time.time()

fibo1 = 1
fibo2 = 1
temp = 0
length = 0
i = 2

while length != 1000:
	temp = fibo1
	fibo1 = fibo2
	fibo2 += temp
	length = len(str(fibo2))
	i += 1

print(i)
print("--- %s seconds ---" % (time.time() - start_time))
