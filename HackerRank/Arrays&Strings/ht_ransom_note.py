def ransom_note(magazine, ransom):
	# Hash magazine word and insert them into table
	table = [[] for _ in range(30)]
	for w in magazine:
		hash_num = hash_func(w)
		table[hash_num].append(w)
	# For each word in ransom note, check if magazine table has that word
	for r in random:
		

def hash_func(x):
	num = 0
	for c in list(x):
		num += int(x)
	return num % 30

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if (answer):
	print("Yes")
else:
	print("No")