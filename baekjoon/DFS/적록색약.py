#10026 #13:53
import sys
sys.stdin=open("적록색약.text","r")
from _collections import deque

def bfs(y,x,t):
    deq=deque()
    visited[y][x]=1
    deq.append([y,x])

    while deq:
        here=deq.popleft()
        y,x=here[0],here[1]

        for dir in range(len(dy)):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if 0<=new_y<n and 0<=new_x<n and not visited[new_y][new_x] and matrix[new_y][new_x]==t:
                deq.append([new_y,new_x])
                visited[new_y][new_x]=1

n=int(input())
matrix=[list(map(str,input())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
cnt=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            temp=matrix[i][j]
            bfs(i,j,temp) #(y,x)좌표와 색깔을 함수의 인자로 전달
            cnt+=1
print(cnt,end=' ')
visited=[[0]*n for _ in range(n)] #visited 재사용 위한 초기화
cnt=0

#R,G를 같은 문자로 보기 위해 변경
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='G':
            matrix[i][j]='R'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            temp=matrix[i][j]
            bfs(i,j,temp)
            cnt+=1
print(cnt)
#16:00