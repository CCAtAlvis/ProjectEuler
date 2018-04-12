import time
start_time = time.clock()

#ans 21124
# zero (0), one, two, three etc
ones = [0, 3, 3, 5, 4, 4, 3, 5, 6, 4]
ones_word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
# ten, eleven, twelve, etc
tens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens_word = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# 0(0), ten (0), twenty, thirty, forty etc
twos = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
two_word = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

sum = i = j = k = 0
word = ''

while i < 10: #hundred counter
	while j < 10: #tens counter
		while k < 10: #ones counter
			if i == 0:
				#sum += ones[i]
				word = ''
			else:
				if j == 0 and k == 0:
					#sum += 7 + ones[i]
					word = word+ones_word[i]+"hundred"
				else :
					word = word+ones_word[i]+"hundredand"
					#sum += 10 + ones[i]

			if j == 0:
				#sum += ones[k]
				word = word+ones_word[k]
			elif j == 1:
				#sum += tens[k]
				word = word+tens_word[k]
			else:
				#sum += twos[j] + ones[k]
				word = word+two_word[j]+ones_word[k]

			sum += len(word)
			print word
			word = ''
			k += 1

		j += 1
		k = 0

	i += 1
	j = k = 0

sum += ones[1] + 8

print sum

print"--- %s seconds ---" % (time.clock() - start_time)
