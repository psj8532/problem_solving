import sys
sys.stdin = open("알고스팟.txt", "r")
from _collections import deque
# import time

# stime = time.time()
#0.1
M,N = map(int,input().split())
direct = [(-1,0),(0,1),(1,0),(0,-1)]
maze = [list(map(int,input())) for _ in range(N)]
INF = float('inf')
dist = [[INF]*M for _ in range(N)]
dist[0][0] = 0
cnt = 0
deq = deque()
deq.append([0,0])
while deq:
    here = deq.popleft()
    i,j = here[0],here[1]
    for dir in range(4):
        y,x = i+direct[dir][0],j+direct[dir][1]
        if 0<=y<N and 0<=x<M and dist[i][j] + maze[y][x] < dist[y][x]:
            dist[y][x] = dist[i][j] + maze[y][x]
            deq.append([y,x])
print(dist[N-1][M-1])
# print('time: {}'.format(time.time()-stime))

#14초
# import time
#
# stime = time.time()
#
# M,N = map(int,input().split())
# direct = [(-1,0),(0,1),(1,0),(0,-1)]
# maze = [list(map(int,input())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# INF = float('inf')
# dist = [[INF]*M for _ in range(N)]
# dist[0][0] = 0
# cnt = 0
# while cnt < N*M:
#     min = INF
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and dist[i][j] < min:
#                 min = dist[i][j]
#                 cur = (i,j)
#     visited[cur[0]][cur[1]] = 1
#     cnt += 1
#     for dir in range(4):
#         y,x = cur[0]+direct[dir][0],cur[1]+direct[dir][1]
#         if 0<=y<N and 0<=x<M and dist[cur[0]][cur[1]] + maze[y][x] < dist[y][x]:
#             dist[y][x] = dist[cur[0]][cur[1]] + maze[y][x]
# print(dist[N-1][M-1])
# print('time: {}'.format(time.time()-stime))

#기존의 코드는 최소 값이 있는 곳의 좌표를 찾는라 매번 2차원 리스트 전부를 돌아야한다.
#하지만 deq을 사용함으로써 어펜드 팝만 하면 되므로 시간을 단축할 수 있다.

#또한, 최소 비용으로 왔던 지점에 도착했을때 그 지점에서 다시 출발하기 위해 2차원 리스트 전체를 돌아야 하지만
#deq을 이용하면 바로 꺼낼 수 있으므로 시간을 단축할 수 있다.