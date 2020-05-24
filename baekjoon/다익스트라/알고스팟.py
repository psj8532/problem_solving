import sys
sys.stdin = open("알고스팟.txt", "r")
import time

stime = time.time()

M,N = map(int,input().split())
direct = [(-1,0),(0,1),(1,0),(0,-1)]
maze = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
INF = float('inf')
dist = [[INF]*M for _ in range(N)]
dist[0][0] = 0
cnt = 0
while cnt < N*M:
    min = INF
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and dist[i][j] < min:
                min = dist[i][j]
                cur = (i,j)
    visited[cur[0]][cur[1]] = 1
    cnt += 1
    for dir in range(4):
        y,x = cur[0]+direct[dir][0],cur[1]+direct[dir][1]
        if 0<=y<N and 0<=x<M and dist[cur[0]][cur[1]] + maze[y][x] < dist[y][x]:
            dist[y][x] = dist[cur[0]][cur[1]] + maze[y][x]
# for row in dist:
#     print(*row)
print(dist[N-1][M-1])
print('time: {}'.format(time.time()-stime))