#3190 #22:25
import sys
sys.stdin=open("뱀.text","r")
from collections import deque
def isExist(new_y,new_x):
    if matrix[new_y][new_x]:
        matrix[new_y][new_x]=0
        return True
    else:
        return False
def isSafe(new_y,new_x):
    if 0<=new_y<n and 0<=new_x<n:
        return True
    else:
        return False
def move(dir,end,t):
    deq=deque()
    y=x=0
    deq.append([y,x])
    visited[y][x]=1

    dy,dx=direct[dir][0],direct[dir][1]
    while isSafe(y+dy,x+dx) and not visited[y+dy][x+dx]:
        t+=1
        y+=dy
        x+=dx
        visited[y][x]=1
        deq.appendleft([y, x])
        if not isExist(y,x):
            ty, tx = deq.pop()
            visited[ty][tx] = 0
        if end<len(data) and t==data[end][0]:
            if data[end][1]=='D':
                dir = direct.index(R[dir])
            else:
                dir=direct.index(L[dir])
            end+=1
            dy, dx = direct[dir][0], direct[dir][1]
    return t+1

n=int(input())
k=int(input())
matrix=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
direct=[[0,1],[1,0],[0,-1],[-1,0]]
R=[[1,0],[0,-1],[-1,0],[0,1]]
L=[[-1,0],[0,1],[1,0],[0,-1]]
for i in range(k):
    y,x=map(int,input().split())
    matrix[y-1][x-1]=1
d=int(input())
data=[list(map(str,input().split())) for _ in range(d)]
for i in range(d):
    data[i][0] = int(data[i][0])

time=move(0,0,0)
print(time)