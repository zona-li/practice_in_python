#!/bin/python3

import sys
import re

def lonely_integer(a):
    s = set()
    for i in a:
    	if i in s:
    		s.remove(i)
    	else:
    		s.add(i)
    return(s.pop())

# Second solution
def lonely_integer(a):
    result = 0
    for i in a:
        result ^= i
    return result

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))