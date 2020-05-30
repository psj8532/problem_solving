def dfs(h):
    while stack:
        here = stack.pop()
        y,x = here[0],here[1]
        if not visited[y][x]:
            visited[y][x] = 1
            for dir in range(4):
                new_y,new_x = y+direct[dir][0],x+direct[dir][1]
                if 0<=new_y<N and 0<=new_x<N and not visited[new_y][new_x] and matrix[new_y][new_x] > h:
                    stack.append((new_y,new_x))

direct = [(-1,0),(0,1),(1,0),(0,-1)]
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
cnt_max = max = 0

for i in range(N):
    for j in range(N):
       if matrix[i][j] > max:
           max = matrix[i][j]
for hg in range(max+1):
    visited = [[0] * N for _ in range(N)]
    stack = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > hg and not visited[i][j]:
                stack.append((i,j))
                dfs(hg)
                cnt += 1
    if cnt > cnt_max:
        cnt_max = cnt

print(cnt_max)