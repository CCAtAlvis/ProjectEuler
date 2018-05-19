import time
start_time = time.time()

def isAbd(x):
	n = int(x/2) + 1
	i = 2
	result = 1

	while i < n:
		if x%i == 0:
			result += i
		i += 1
	return result > x

abundant = []

result = 0
i = 12
limit = 28123
while i <= limit:
	if isAbd(i):
		abundant.append(i)

	# for a in abundant:
	# 	#check = i - a
	# 	if a<i and (i-a) in abundant:
	# 		break
	# else:
	# 	result += i

	i += 1

canBeWrittenAsAbd = []

for i in range(limit):
	canBeWrittenAsAbd.append(False)

for i in range(len(abundant)):
	for j in range(i, len(abundant)):
		if abundant[i] + abundant[j] < limit:
			canBeWrittenAsAbd[abundant[i] + abundant[j]] = True
		else:
			break

for i in range(len(canBeWrittenAsAbd)):
	if not canBeWrittenAsAbd[i]:
		result += i

print(result)
print("--- %s seconds ---" % (time.time() - start_time))
