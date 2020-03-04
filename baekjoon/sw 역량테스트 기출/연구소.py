import sys
sys.stdin = open("연구소.text","r")
from collections import deque

def bfs():
    deq = deque()
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==2:
                deq.append([i,j])
    while deq:
        here = deq.popleft()
        y,x=here[0],here[1]
        for dir in range(len(dy)):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if 0<=new_y<r and 0<=new_x<c and not matrix[new_y][new_x]:
                deq.append([new_y,new_x])
                matrix[new_y][new_x]=3


r,c = map(int,input().split())
matrix=[]
visited=[]
cnt=0
max_val=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for _ in range(r):
    matrix.append(list(map(int,input().split())))

for y in range(r):
    for x in range(c):
        if not matrix[y][x]:
            visited.append([y,x])

n=len(visited)
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            matrix[visited[i][0]][visited[i][1]]=1
            matrix[visited[j][0]][visited[j][1]]=1
            matrix[visited[k][0]][visited[k][1]]=1
            bfs()
            count=0
            for y in range(r):
                for x in range(c):
                    if not matrix[y][x]:
                        count+=1

            if max_val<count:
                max_val=count
            matrix[visited[i][0]][visited[i][1]] = 0
            matrix[visited[j][0]][visited[j][1]] = 0
            matrix[visited[k][0]][visited[k][1]] = 0
            for y in range(r):
                for x in range(c):
                    if matrix[y][x]==3:
                        matrix[y][x]=0
print(max_val)