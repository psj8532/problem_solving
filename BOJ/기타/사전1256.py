from itertools import permutations

N, M, K = map(int,input().split())
s = 'a' * N + 'z' * M
perm = sorted(set(list(permutations(s, N+M))))
total = len(perm)
if K > total: print(-1)
else: print(''.join(perm[K-1]))