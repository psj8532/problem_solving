from itertools import permutations

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
sorted_numbers = sorted(numbers)

perm = set(list(permutations(sorted_numbers, M)))
perm = sorted(set(perm))
for p in perm:
    print(*p)
