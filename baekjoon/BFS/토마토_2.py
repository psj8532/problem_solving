#7569 #22:47
#3중 for문 돌려서 0의 갯수 세고, 마지막에 cnt가 0보다 크면 다 익지 못하는 상황임
#dx,dy,dz

import sys
sys.stdin=open("토마토_2.text","r")
from collections import deque

def bfs():
    global count,max_cnt
    while deq:
        here = deq.popleft()
        z,y,x,depth = here[0],here[1],here[2],here[3]

        for dir in range(len(dy)):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if 0<=new_y<r and 0<=new_x<c and not matrix[z][new_y][new_x]:
                deq.append([z,new_y,new_x,depth+1])
                matrix[z][new_y][new_x]=1
                count-=1
        for dir_z in range(len(dz)):
            new_z = z + dz[dir_z]
            if 0<=new_z<h and not matrix[new_z][y][x]:
                deq.append([new_z,y,x,depth+1])
                matrix[new_z][y][x]=1
                count-=1
    return depth

c,r,h = map(int,input().split())
matrix=[[list(map(int,input().split())) for row in range(r)] for height in range(h)]
deq=deque()
count=0
dz=[1,0,-1]
dy=[-1,0,1,0]
dx=[0,1,0,-1]

for z in range(h):
    for y in range(r):
        for x in range(c):
            if matrix[z][y][x]==1:
                deq.append([z,y,x,0])
            elif not matrix[z][y][x]:
                count+=1
result=bfs()
if count>0:
    print(-1)
else:
    print(result)