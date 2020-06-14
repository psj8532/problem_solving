from _collections import deque

def change(y,x,v):
    deq = deque()
    deq.append((y,x))
    visited[y][x] = 1
    matrix[y][x] = v
    while deq:
        here = deq.popleft()
        y,x = here[0],here[1]
        for dir in range(4):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<N and not visited[new_y][new_x] and matrix[new_y][new_x]:
                deq.append((new_y,new_x))
                visited[new_y][new_x] = 1
                matrix[new_y][new_x] = v


def bfs(y,x,v,cnt):
    global min
    deq = deque()
    visited = [[0]*N for _ in range(N)]
    deq.append((y,x,cnt))
    visited[y][x] = 1
    while deq:
        here = deq.popleft()
        y,x,cnt = here[0],here[1],here[2]
        for dir in range(4):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<N:
                if matrix[new_y][new_x] == v and not visited[new_y][new_x] and not cnt: #같은 육지인데 방문하지 않은 곳이고 다리를 세운 적이 없다면
                    visited[new_y][new_x] = -1
                    deq.append((new_y,new_x,cnt))
                if matrix[new_y][new_x] and matrix[new_y][new_x] != v: #다른 육지라면
                    #cnt로 비교 #다리연결 완료
                    if cnt < min:
                        min = cnt
                if not matrix[new_y][new_x] and not visited[new_y][new_x]: #바다라면 visited가 -1일 수 없음
                    visited[new_y][new_x] = cnt+1
                    deq.append((new_y,new_x,cnt+1))
                if not matrix[new_y][new_x] and cnt+1 < visited[new_y][new_x]: #바다인데 다리갯수를 최소로세울 수 있다면
                    visited[new_y][new_x] = cnt+1
                    deq.append((new_y,new_x,cnt+1))


direct = [(-1,0),(0,1),(1,0),(0,-1)]
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
val = 0
min = 987654321
for i in range(N):
    for j in range(N):
        if matrix[i][j] and not visited[i][j]:
            val += 1
            change(i,j,val)
val = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] > val:
            val += 1
            bfs(i,j,matrix[i][j],0)
print(min)