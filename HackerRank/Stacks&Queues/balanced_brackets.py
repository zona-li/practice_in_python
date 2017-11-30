def is_matched(expression):
	stack = []
	if len(expression) % 2 != 0:
		return False
	for c in expression:
		if not stack:	# stack is empty
			stack.append(c)
		else:
			end_char = stack.pop()
			if ord(c)-1 == ord(end_char) or ord(c)-2 == ord(end_char):
				pass
			else:
				stack.append(end_char)
				stack.append(c)
	return not stack


t = int(input().strip())
for a0 in range(t):
	expression = input().strip()
	if is_matched(expression) == True:
		print("YES")
	else:
		print("NO")