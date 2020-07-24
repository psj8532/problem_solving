def dfs(index,y,x,f):
    global cnt, count
    if index == data[0]:
        if not f:
            cnt += 1
        count += 1
    else:
        for dir in range(1,5):
            if data[dir]:
                ny, nx = y + direct[dir][0], x + direct[dir][1]
                if visited[ny][nx]:
                    dfs(index+1,ny,nx,True)
                else:
                    visited[ny][nx] = 1
                    dfs(index+1,ny,nx,False)
                    visited[ny][nx] = 0


direct = [(0,0),(0,1),(0,-1),(1,0),(0,-1)]
data = list(map(int,input().split()))
visited = [[0]*(2*data[0]+1) for _ in range(2*data[0]+1)]
cnt = count = 0
visited[data[0]][data[0]] = 1
flag = False
dfs(0,data[0],data[0],flag)
print(cnt/count)