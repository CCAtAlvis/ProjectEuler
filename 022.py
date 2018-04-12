#time to be smart... less fun but... less coding time also
#using in-built algos now :) :(
import time
start_time = time.time()

def score(x,y):
	i = 0
	score = 0

	while i < len(x):
		score += ord(x[i]) - 64
		i += 1
	return y*score 

f = open("022_names.txt", "r")
file = f.read().split(",")

name = ""
names = []
sum = i = 0

for name in file:
	name = name[1:-1]
	names.append(name)

#while i < len(file):
#	if file[i] == "\"":
#		name = name
#	elif file[i] == ",":
#		names.append(name)
#		name = ""
#	else:
#		name += file[i]
#	i += 1

#the for loop algo seems to work but the if doesnt...
#look into that later...
#but do look into it 

names.sort()
i = 0

while i < len(names):
	sum += score(names[i], i+1)
	i += 1

print sum
print("--- %s seconds ---" % (time.time() - start_time))
