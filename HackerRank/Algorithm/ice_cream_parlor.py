import sys

def solve(arr, money):
    cost_map = {}
    for i, cost in enumerate(arr):
        sunny = money - cost
        if sunny in cost_map.keys():
            print(cost_map[sunny]+1, i+1)
        else:
            cost_map[cost] = i


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)