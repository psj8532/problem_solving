N, M = map(int,input().split())
INF = float('inf')
relation = [[INF] * (N + 1) for _ in range(N+1)]
answer = INF
min_bacon = INF
for _ in range(M):
    s,e = map(int,input().split())
    relation[s][e], relation[e][s] = 1, 1
for i in range(1, N + 1):
    relation[i][i] = 0

for m in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cost = relation[i][m] + relation[m][j]
            if cost < relation[i][j]:
                relation[i][j], relation[j][i] = cost, cost

for i in range(1, N + 1):
    kevin_bacon = 0
    for j in range(1, N + 1):
        kevin_bacon += relation[i][j]
    if kevin_bacon < min_bacon:
        min_bacon = kevin_bacon
        answer = i

print(answer)