def ransom_note(magazine, ransom):
	

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