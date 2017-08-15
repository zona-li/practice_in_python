def number_needed(a, b):
	counter = 0
	print(len(a))
	print(a.count("a"))
	print(b.count("a"))
	print(b.find("z"))

	for c in a:
		if b.find("c") != -1:
			counter++
			b.remove("c")
		else:
			pass

def test_program():
	a = "asdlkf"
	if a.find("z") != -1:
		return 

a = 'cde'
b = 'abc'

# print(number_needed(a, b))

print(test_program())