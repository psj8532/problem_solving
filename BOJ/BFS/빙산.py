from _collections import deque

def copy(o,n):
    for i in range(N):
        for j in range(M):
            n[i][j] = o[i][j]

def dfs(y,x,v,mat):
    stack = [(y,x)]
    while stack:
        h = stack.pop()
        y,x = h[0],h[1]
        if not v[y][x]:
            v[y][x] = 1
            for dir in range(4):
                ny,nx = y+direct[dir][0],x+direct[dir][1]
                if 0<=ny<N and 0<=nx<M and not v[ny][nx] and mat[ny][nx]:
                    stack.append((ny,nx))

def check(m):
    visited = [[0]*M for _ in range(N)]
    c = 0
    for i in range(N):
        for j in range(M):
            if m[i][j]>0 and not visited[i][j]:
                if c > 0: return True
                dfs(i,j,visited,m)
                c+=1
    return False

def bfs():
    d_pre = -1
    while deq:
        here = deq.popleft()
        y,x,d = here[0],here[1],here[2]
        if d_pre != d:
            copy(temp, matrix)
            if check(matrix):
                return d
        d_pre = d
        cnt = 0
        for dir in range(4):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<M and not matrix[new_y][new_x]:
                cnt += 1
        temp[y][x] -= cnt
        if temp[y][x] < 0: temp[y][x] = 0
        elif temp[y][x] > 0: deq.append((y,x,d+1))
    return False

direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
temp = [[0]*M for _ in range(N)]
deq = deque()
copy(matrix,temp)
for i in range(N):
    for j in range(M):
        if temp[i][j] > 0:
            deq.append((i,j,0))
ans = bfs()
if not ans:
    ans = 0
print(ans)