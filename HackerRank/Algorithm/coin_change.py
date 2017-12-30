#!/bin/python3

import sys

def make_change(coins, n):
    count = 0
    for c in coins:
    	count += make_change(coins, n-c)
    return count

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
