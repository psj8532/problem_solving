# 11:56 ~ 12:10 (Time Over)
# 플로이드의 경우 800^3이 걸리기 때문에 총 5억1200만초가 걸린다.
# 20억 이하이므로 시간초과가 안날줄 알았는데 발생했다.
# 플로이드
N, E = map(int,input().split())
INF = float('inf')
dist = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    dist[i][i] = 0
for _ in range(E):
    s, e, c = map(int,input().split())
    dist[s][e] = min(dist[s][e], c)
    dist[e][s] = min(dist[e][s], c)
v1, v2 = map(int,input().split())
for m in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            c = dist[i][m] + dist[m][j]
            dist[i][j] = min(dist[i][j], c)
ans1 = dist[1][v1] + dist[v1][v2] + dist[v2][N]
ans2 = dist[1][v2] + dist[v2][v1] + dist[v1][N]
answer = min(ans1, ans2)
if answer == INF: print(-1)
else: print(answer)