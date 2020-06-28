from _collections import deque
import heapq


def change(y,x,v):
    deq = deque()
    deq.append((y,x,v))
    matrix[y][x] = v
    visited[y][x] = 1
    while deq:
        here = deq.popleft()
        y,x,v = here[0],here[1],here[2]
        for dir in range(4):
            ny,nx = y+direct[dir][0],x+direct[dir][1]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and matrix[ny][nx]:
                deq.append((ny,nx,v))
                visited[ny][nx] = 1
                matrix[ny][nx] = v


def bfs(y,x,c,v):
    deq = deque()
    for dir in range(4):
        ny,nx = y+direct[dir][0],x+direct[dir][1]
        if 0<=ny<N and 0<=nx<M and not matrix[ny][nx]:
            deq.append((ny,nx,c+1,dir))
    while deq:
        here = deq.popleft()
        y,x,c,dir = here[0],here[1],here[2],here[3]
        ny,nx = y+direct[dir][0],x+direct[dir][1]
        if 0<=ny<N and 0<=nx<M and c>=2 and matrix[ny][nx] and matrix[ny][nx]!=v and c < adj[v][matrix[ny][nx]]:
            adj[v][matrix[ny][nx]] = c
            adj[matrix[ny][nx]][v] = c
        elif 0<=ny<N and 0<=nx<M and not matrix[ny][nx]:
            deq.append((ny,nx,c+1,dir))


direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
INF = float('inf')
count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and matrix[i][j]:
            count += 1
            change(i,j,count)

adj = [[INF]*(count+1) for _ in range(count+1)]
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            bfs(i,j,0,matrix[i][j])

heap = []
mst = [0]*(count+1)
key = [INF]*(count+1)
key[1] = 0
result = 0
heapq.heappush(heap, (0,1))
while heap:
    min,u = heapq.heappop(heap)
    if mst[u]: continue
    mst[u] = 1
    result += min
    for w in range(1,count+1):
        if not mst[w] and adj[u][w] < key[w]:
            key[w] = adj[u][w]
            heapq.heappush(heap, (key[w],w))

for i in range(1,count+1):
    if not mst[i]:
        print(-1)
        break
else:
    print(result)
