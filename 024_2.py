# this is iterrative approach to the question
import time
start_time = time.time()

from math import factorial

permu = 1000000
combi = ""
numbers = list(i for i in range(0,10))
n = len(numbers)

for i in range(1, n):
    j = permu // factorial(n-i)
    print(numbers, end=" \t")
    permu = permu % factorial(n-i)
    combi = combi + str(numbers[j])
    del numbers[j]
    print(j, numbers)

    if permu == 0:
        break

print(combi)
print("--- %s seconds ---" % (time.time() - start_time))
