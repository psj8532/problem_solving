from _collections import deque

def bfs(y,x,d):
    deq=deque()
    deq.append((y,x,d))
    Visited[y][x]=1

    while deq:
        here=deq.popleft()
        y,x,d=here[0],here[1],here[2]
        for dir in range(len(direct)):
            new_y,new_x=y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<r and 0<=new_x<c and not Visited[new_y][new_x] and Matrix[new_y][new_x]=='L':
                deq.append((new_y,new_x,d+1))
                Visited[new_y][new_x]=1
    return d
direct=[(-1,0),(0,1),(1,0),(0,-1)]
r,c=map(int,input().split())
Matrix=[list(map(str,input())) for _ in range(r)]
depth_max=-1
for i in range(r):
    for j in range(c):
        if Matrix[i][j]=='L':
            Visited=[[0]*c for _ in range(r)]
            depth=bfs(i,j,0)
            if depth>depth_max:
                depth_max=depth
print(depth_max)