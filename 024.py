# this is iterrative approach to the question
import time
start_time = time.time()

import math

i = 0
add = 0
fact = 9
permu = 0
combi = 0

while permu != 1000000:
	if permu > 1000000:
		print(combi)
		permu = permu - math.factorial(fact)
		combi = combi*10 + (i-1+add)
		i = 0
		fact -= 1
		add += 1
	else:
		permu = permu + math.factorial(fact)
		i += 1

print(permu)
print(combi)
print("--- %s seconds ---" % (time.time() - start_time))
