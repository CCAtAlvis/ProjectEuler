import time
start_time = time.time()

#my first recursion in python yaaa....
def fact(x):
	if x > 1:
		return x*fact(x-1)
	else :
		return 1;
#... or i could have used math.factorial :(
#but recursion... lets just stick to it for now

num = fact(100)
num = str(num)

i = sum = 0

while i < len(num):
	sum += int(num[i])
	i += 1

print sum
print("--- %s seconds ---" % (time.time() - start_time))
