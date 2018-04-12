import time
import math
start_time = time.clock()

num = math.factorial(40)/math.factorial(20)
num = num/math.factorial(20)

print num

print"--- %s seconds ---" % (time.clock() - start_time)
