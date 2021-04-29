from itertools import combinations

N, M = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
comb = sorted(set(list(combinations(numbers, M))))
for c in comb:
    print(*c)
