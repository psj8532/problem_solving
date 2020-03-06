#10026 #13:53
#적록색약이 아닌 사람이 봤을때는 다른 글자가 나올때까지
#적록색약인 사람은 R이나 G이면 같은색으로 인식
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
            bfs(i,j,temp)
            cnt+=1
print(cnt,end=' ')
visited=[[0]*n for _ in range(n)]
cnt=0
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