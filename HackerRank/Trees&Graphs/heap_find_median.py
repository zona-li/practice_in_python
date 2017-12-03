import sys

def calculate_median(a_t):
	if len(a) == 1:
		return(a_t)
	if len(a) == 2:
		return(average(a[0], a[1]))
	if len(a)%2 == 1:
		index = int((len(a)-1) / 2)
		return(a[index])
	else:
		return(average(a[int(len(a)/2)], a[int(len(a)/2 - 1)]))


def average(a, b):
	return (a+b)/2

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
	a_t = int(input().strip())
	a.append(a_t)
	a.sort()
	print("%.1f" % calculate_median(a_t))

