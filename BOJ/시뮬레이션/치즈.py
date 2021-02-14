# 17:44 ~ 18:19
from _collections import deque

def check(c):
    deq = deque([[0,0]])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while deq:
        y, x = deq.popleft()
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= ny < N and 0 <= nx < M and paper[ny][nx] and (ny, nx) in c:
                c[(ny, nx)] += 1
            elif 0 <= ny < N and 0 <= nx < M and paper[ny][nx]:
                c[(ny, nx)] = 1
            elif 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = 1
                deq.append([ny, nx])
    return c

dy, dx = [-1,0,1,0], [0,1,0,-1]
N, M = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(N)]
time = 0
while 1:
    cheeze = check({})
    if not cheeze: break
    time += 1
    for position, cnt in cheeze.items():
        if cnt < 2: continue
        paper[position[0]][position[1]] = 0
print(time)