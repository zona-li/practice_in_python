def ransom_note(magazine, ransom):
	rc = {} # dict of word: count of that word in the note
    for word in ransom:
        if word not in rc:
            rc[word] = 0
        rc[word] += 1
    
    for word in magazine:
        if word in rc:
            rc[word] -= 1
            if rc[word] == 0:
                del rc[word]
                if not rc:
                    return True
    return False


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if (answer):
	print("Yes")
else:
	print("No")