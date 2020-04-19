import sys
sys.stdin = open("아기상어.txt","r")
from _collections import deque

def bfs(y,x,d):
    global charge
    flag = 0
    s=[]
    visited = [[0]*n for _ in range(n)]
    deq=deque()
    deq.append((y,x,d))
    visited[y][x]=1

    while deq:
        here = deq.popleft()
        y,x,d = here[0],here[1],here[2]
        if flag and s:
            if temp==d:
                pass
            else:
                min_y, min_x, d = s[0][0], s[0][1], s[0][2]
                for i in range(1, len(s)):
                    if s[i][0] < min_y:
                        min_y, min_x = s[i][0], s[i][1]
                    elif s[i][0] == min_y and min_x > s[i][1]:
                        min_y, min_x = s[i][0], s[i][1]
                matrix[min_y][min_x] = 0
                charge += 1
                return (min_y, min_x, d)

        for next in range(len(direct)):
            new_y,new_x = y + direct[next][0],x+direct[next][1]
            if 0<=new_y<n and 0<=new_x<n and 0<matrix[new_y][new_x]<shark_size and not visited[new_y][new_x]:
                s.append((new_y,new_x,d+1))
                visited[new_y][new_x]=1
            elif not s and 0<=new_y<n and 0<=new_x<n and matrix[new_y][new_x]<=shark_size and not visited[new_y][new_x]:
                deq.append((new_y,new_x,d+1))
                visited[new_y][new_x]=1
        if s:
            temp = d
            flag = 1
            if not deq:
                min_y, min_x, d = s[0][0], s[0][1], s[0][2]
                for i in range(1, len(s)):
                    if s[i][0] < min_y:
                        min_y, min_x = s[i][0], s[i][1]
                    elif s[i][0] == min_y and min_x > s[i][1]:
                        min_y, min_x = s[i][0], s[i][1]
                matrix[min_y][min_x] = 0
                charge += 1
                return (min_y, min_x, d)

    return False

direct=[(-1,0),(0,1),(1,0),(0,-1)]
n=int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
shark_size = 2
charge = 0
t=0

for i in range(n):
    for j in range(n):
        if matrix[i][j]==9:
            posi = (i,j,0)
            matrix[i][j]=0
            break
while posi:
    posi = bfs(posi[0],posi[1],0)
    if posi:
        t+=posi[2]
    if shark_size==charge:
        shark_size += 1
        charge = 0

print(t)