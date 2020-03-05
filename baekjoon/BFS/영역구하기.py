#2583 #20:42
import sys
sys.stdin=open("영역구하기.text","r")

def bfs(cnt):
    cnt+=1
    while queue:
        here = queue.pop(0)
        y,x=here[0],here[1]
        for dir in range(len(dy)):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if 0<=new_y<n and 0<=new_x<m and not matrix[new_y][new_x]:
                queue.append([new_y,new_x])
                matrix[new_y][new_x]=2
                cnt+=1
    return cnt

dy=[-1,0,1,0]
dx=[0,1,0,-1]
n,m,k=map(int,input().split()) #n:세로길이, m:가로길이, 부분직사각형의 갯수
data=[]
queue=[]
result=[]
for _ in range(k):
    data.append(list(map(int,input().split())))
matrix = [[0]*m for _ in range(n)]
for i in range(k):
    y1,y2=data[i][1],data[i][3]
    x1,x2=data[i][0],data[i][2]
    for y in range(y1,y2):
        for x in range(x1,x2):
            matrix[y][x]=1

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            queue.append([i,j])
            matrix[i][j]=2
            temp = bfs(0)
            result.append(temp)
result.sort()

print(len(result))
print(*result)
#21:05