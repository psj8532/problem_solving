from _collections import deque


def find():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                virus.append((i,j))

def combination(index):
    if index == M:
        temp = a[:]
        comb.append(temp)
    else:
        in_perm = [False]*n
        for i in range(index):
            in_perm[a[i]] = True
        for i in range(n-1,-1,-1):
            if in_perm[i]:
                posi = i + 1
                break
        else:
            posi = 0
        c = [0] * n
        cnt = 0
        for i in range(posi,n):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[index] = c[i]
            combination(index+1)

def time_check():
    max = -1
    isSuccess = True
    for y in range(N):
        for x in range(N):
            if visited[y][x] > max:
                max = visited[y][x]
            elif visited[y][x] == -1 and not matrix[y][x]:
                isSuccess = False
    if isSuccess:
        return max+1
    else:
        return isSuccess

def bfs():
    while deq:
        here = deq.popleft()
        y, x, time = here[0], here[1], here[2]
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 2 and visited[ny][nx] == -1:
                deq.append((ny,nx,time+1))
                visited[ny][nx] = 0
            elif 0 <= ny < N and 0 <= nx < N and not matrix[ny][nx] and visited[ny][nx] == -1:
                deq.append((ny,nx,time+1))
                visited[ny][nx] = time+1

direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
virus = []
find()
n = len(virus)
a = [0] * M
comb = []
combination(0)
min = 987654321
isFail = True
for idx in range(len(comb)):
    deq = deque()
    visited = [[-1]*N for _ in range(N)]
    for i in range(M):
        y,x = virus[comb[idx][i]][0],virus[comb[idx][i]][1]
        deq.append((y,x,0))
        visited[y][x] = 0
    bfs()
    ans = time_check()
    if ans and ans-1 < min:
        min = ans-1
        isFail = False
else:
    if isFail:
        print(-1)
    else:
        print(min)