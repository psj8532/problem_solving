def nextFind(r,c,D):
    global cnt
    for _ in range(4):
        dy, dx, D = direct[dir[D]][0],direct[dir[D]][1],dir[D]
        new_y,new_x=r+dy,c+dx
        if 0<=new_y<n and 0<=new_x<m and not matrix[new_y][new_x] and not visited[new_y][new_x]:
            visited[new_y][new_x]=1
            cnt+=1
            return new_y,new_x,D
    return -10,-10,D

def sweep(y,x,d):
    global cnt
    visited[y][x]=1
    cnt+=1

    while y!=-10:
        y_temp, x_temp = y, x
        y, x, d = nextFind(y, x, d)
        while y!=-10:
            y_temp,x_temp=y,x
            y, x, d = nextFind(y, x, d)
        y,x=y_temp,x_temp
        y-=direct[d][0]
        x-=direct[d][1]
        if matrix[y][x]:
            return

n,m=map(int,input().split())
r,c,d=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
dir=[3,0,1,2]
direct=[(-1,0),(0,1),(1,0),(0,-1)]
visited=[[0]*m for _ in range(n)]
cnt=0
sweep(r,c,d)
print(cnt)