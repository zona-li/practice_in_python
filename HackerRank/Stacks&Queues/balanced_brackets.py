def is_matched(expression):
	stack = []
	for c in expression:
		stack.append(c)
	size = len(stack)
	if size % 2 != 0:
		return False
	first_half = []
	second_half = []
	half_size = int(size/2)
	for c in range(0, half_size):
		first_half.append(stack[c])
	for c in range(half_size, size):
		c = stack.pop()
		if c == ")":
			second_half.append("(")
		if c == "]":
			second_half.append("[")
		if c == "}":
			second_half.append("{")
	return first_half == second_half

t = int(input().strip())
for a0 in range(t):
	expression = input().strip()
	if is_matched(expression) == True:
		print("YES")
	else:
		print("NO")