def dfs(y,x,shape):
    global cnt
    if y == N-1 and x == N-1:
        cnt += 1
        return
    if shape == 0:
        if x + 1 < N and not matrix[y][x+1]:
            dfs(y,x+1,0)
        if y + 1 < N and x + 1 < N and not matrix[y+1][x+1] and not matrix[y][x+1] and not matrix[y+1][x]:
            dfs(y+1,x+1,2)
    elif shape == 1:
        if y + 1 < N and not matrix[y+1][x]:
            dfs(y+1,x,1)
        if y + 1 < N and x + 1 < N and not matrix[y+1][x+1] and not matrix[y][x+1] and not matrix[y+1][x]:
            dfs(y+1,x+1,2)
    elif shape == 2 :
        if x + 1 < N and not matrix[y][x+1]:
           dfs(y,x+1,0)
        if y + 1 < N and not matrix[y+1][x]:
           dfs(y+1,x,1)
        if y + 1 < N and x + 1 < N and not matrix[y+1][x+1] and not matrix[y][x+1] and not matrix[y+1][x]:
           dfs(y+1,x+1,2)


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
dfs(0,1,0)
print(cnt)