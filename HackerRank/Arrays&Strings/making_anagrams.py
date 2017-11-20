def number_needed(first, second):
	a = [0] * 26
	b = [0] * 26
	answer = 0

	for i in range(len(first)):
		num = ord(first[i]) - 97			# 'num' stores the number that corresponds to the letter
		counter = a[num]
		counter += 1
		a[num] = counter					# Update the array to reflect how many each letter does the string has

	# Do the same for the second string
	for i in range(len(second)):
		num = ord(second[i]) - 97			
		counter = b[num]
		counter += 1
		b[num] = counter

	for i in range(0,26):
		answer += abs(a[i] - b[i])
	return answer

print(number_needed("skdjhflksdfjhasddkfjhy", "skdjfbkasjdhfkjandfadz"))