# 15:00 ~ 15:16
# 주의: 갈 수 없는 루트의 경우 0을 출력해야 된다.
N = int(input())
M = int(input())
INF = float('inf')
cities = [[INF] * N for _ in range(N)]
for i in range(N):
    cities[i][i] = 0
for _ in range(M):
    start, end, cost = map(int,input().split())
    start, end = start - 1, end - 1
    cities[start][end] = min(cities[start][end], cost)

for m in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            cost = cities[i][m] + cities[m][j]
            cities[i][j] = min(cities[i][j], cost)

for i in range(N):
    for j in range(N):
        if cities[i][j] == INF: cities[i][j] = 0

for row in cities:
    print(*row)