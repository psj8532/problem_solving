#2178 #17:33
import sys
sys.stdin = open("미로탐색.text","r")

def bfs(y,x):
    queue=[]
    a=1
    queue.append([y,x,a])
    visited[y][x]=1

    while queue:
        here = queue.pop(0)
        a=here[2]
        if here[0]==n-1 and here[1]==m-1:
            return a
        for dir in range(len(dy)):
            y,x=here[0],here[1]
            new_y,new_x =y+dy[dir],x+dx[dir]
            if 0<=new_y<n and 0<=new_x<m and matrix[new_y][new_x] and not visited[new_y][new_x]:
                queue.append([new_y,new_x,a+1])
                visited[new_y][new_x]=1

n,m = map(int,input().split())
dy=[-1,0,1,0]
dx=[0,1,0,-1]
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input())))
visited=[[0]*m for _ in range(n)]
depth = bfs(0,0)
print(depth)
#19:58


# #이차원 리스트에 뎁스저장
# def bfs(y,x):
#     queue=[]
#     queue.append([y,x])
#     visited[y][x]=1
#     depth[y][x]=1
#     while queue:
#         here = queue.pop(0)
#         if here[0]==n-1 and here[1]==m-1:
#             print(depth[here[0]][here[1]])
#             return
#         for dir in range(len(dy)):
#             y,x = here[0],here[1]
#             new_y,new_x=y+dy[dir],x+dx[dir]
#             if 0<=new_y<n and 0<=new_x<m and matrix[new_y][new_x] and not visited[new_y][new_x]:
#                 queue.append([new_y,new_x])
#                 visited[new_y][new_x]=1
#                 depth[new_y][new_x]=depth[y][x]+1
#
# n,m = map(int,input().split())
# dy=[-1,0,1,0]
# dx=[0,1,0,-1]
# matrix=[]
# for _ in range(n):
#     matrix.append(list(map(int,input())))
# visited=[[0]*m for _ in range(n)]
# depth=[[0]*m for _ in range(n)]
# bfs(0,0)