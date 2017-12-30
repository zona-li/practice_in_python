#!/bin/python3

import sys

def make_change(coins, n):
    count = [0 for _ in range(n+1)]
    count[0] = 1
    for coin in coins:
    	for i in range(coin, n+1):
    		count[i] += count[i-coin]
    return count[n]

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
