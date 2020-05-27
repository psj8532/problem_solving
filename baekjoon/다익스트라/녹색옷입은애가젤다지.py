import sys
sys.stdin = open("녹색옷입은애가젤다지.txt", "r")
from _collections import deque

direct = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
while 1:
    N = int(input())
    if N == 0:
        break
    cnt += 1
    matrix = [list(map(int,input().split())) for _ in range(N)]
    INF = float('inf')
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = matrix[0][0]
    deq = deque()
    deq.append((0,0))
    while deq:
        here = deq.popleft()
        y,x = here[0],here[1]
        for dir in range(4):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<N and dist[y][x] + matrix[new_y][new_x] < dist[new_y][new_x]:
                dist[new_y][new_x] = dist[y][x] + matrix[new_y][new_x]
                deq.append((new_y,new_x))
    print('Problem {}: {}'.format(cnt, dist[N-1][N-1]))