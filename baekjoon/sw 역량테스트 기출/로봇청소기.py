import sys
sys.stdin=open("로봇청소기.txt","r")

# def detect(y,x,D):
#     global cnt
#     visited[y][x]=1
#     cnt+=1
#     for _ in range(4):
#         dy, dx, D = direct[dir[D]][0],direct[dir[D]][1],dir[D]
#         new_y,new_x=y+dy,x+dx
#         if 0<=new_y<n and 0<=new_x<m and not matrix[new_y][new_x] and not visited[new_y][new_x]:
#             detect(new_y,new_x,D)
#     else:
#         D=(D+2)%4
#         dy, dx= direct[dir[D]][0],direct[dir[D]][1]
#         new_y, new_x = y + dy, x + dx
#         if 0<=new_y<n and 0<=new_x<m and matrix[new_y][new_x] and visited[new_y][new_x]:
#             return
#         detect(new_y,new_x,D)
#         return

def nextFind(r,c,D):
    for _ in range(4):
        dy, dx, D = direct[dir[D]][0],direct[dir[D]][1],dir[D]
        new_y,new_x=r+dy,c+dx
        if 0<=new_y<n and 0<=new_x<m and not matrix[new_y][new_x] and not visited[new_y][new_x]:
            return new_y,new_x,D
    return -10,-10,-10
def sweep(y,x,D):
    global cnt
    visited[y][x]=1
    stack.append((y,x,D))
    cnt+=1
    while stack:
        y,x,D= nextFind(y,x,D)
        if (y,x,D)!=(-10,-10,-10):
            stack.append((y,x,D))
            visited[y][x]=1
            cnt+=1
            d_temp = D
        else:#후진 할 때 왔던길을 돌아가는 것이 아니라, 그 방향 정보 가진채로 가는 것이다
            y,x,D=stack.pop()
            if 0<=y<n and 0<=x<m and nextFind(y,x,D)==(-10,-10,-10):
                #후진했을때의 방향으로 한번더 뒤 살펴봄
                if matrix[direct[dir[d_temp]][0]][direct[dir[d_temp]][1]]:
                    return
            elif 0<=y<n and 0<=x<m and nextFind(y,x,D)!=(-10,-10,-10):
                stack.append((y,x,D))


n,m=map(int,input().split())
r,c,d=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
dir=[3,0,1,2]
direct=[(-1,0),(0,1),(1,0),(0,-1)]
visited=[[0]*m for _ in range(n)]
cnt=0
stack=[]
sweep(r,c,d)
print(cnt)