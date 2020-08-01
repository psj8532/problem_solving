from _collections import deque


def count():
    counter = 0
    for i in range(1,r-1):
        for j in range(1,c-1):
            if matrix[i][j] == 1:
                counter += 1
    return counter


def bfs(y,x):
    deq.append((y,x))
    while deq:
        h = deq.popleft()
        y,x = h[0],h[1]
        for dir in range(4):
            ny,nx = y+direct[dir][0],x+direct[dir][1]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and matrix[ny][nx] == 1:
                visited[ny][nx] = 1
                matrix[ny][nx] = 0
            elif 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and matrix[ny][nx] == 0:
                visited[ny][nx] = 1
                deq.append((ny,nx))


direct = [(-1,0),(0,1),(1,0),(0,-1)]
r,c = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(r)]
t = 0
pre_cnt = 0
while 1:
    cnt = count()
    if cnt == 0: break
    pre_cnt = cnt
    visited = [[0]*c for _ in range(r)]
    deq = deque()
    bfs(1,0)
    t += 1

print(t)
print(pre_cnt)