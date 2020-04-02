#17144
import sys
sys.stdin=open("미세먼지안녕.txt","r")

def move():
    for y in range(r):
        for x in range(c):
            if matrix[y][x] and matrix[y][x]!=-1:
                cnt=0
                temp=matrix[y][x]//5
                for dir in direct:
                    new_y,new_x=y+dir[0],x+dir[1]
                    if 0<=new_y<r and 0<=new_x<c and matrix[new_y][new_x]!=-1:
                        matrix_temp[new_y][new_x]+=temp
                        cnt+=1
                matrix_temp[y][x]+=matrix[y][x]-(temp*cnt)
    for y in range(r):
        for x in range(c):
            matrix[y][x]=matrix_temp[y][x]
            matrix_temp[y][x]=0
    for i in range(2):
        matrix[sweeper[i][0]][sweeper[i][1]]=-1

def sweep(y,x,d,num):
    new_y=new_x=-10
    temp=0
    while (new_y,new_x)!=(sweeper[num][0],sweeper[num][1]):
        new_y,new_x=y+direct[d][0],x+direct[d][1]
        if not num:
            if 0<=new_y<=sweeper[num][0] and 0<=new_x<c:
                val = temp
                temp = matrix[new_y][new_x]
                matrix[new_y][new_x] = val
                y, x = new_y, new_x
            else:
                d = (d - 1) % 4
        else:
            if sweeper[num][0]<=new_y<r and 0<=new_x<c:
                val=temp
                temp=matrix[new_y][new_x]
                matrix[new_y][new_x]=val
                y,x=new_y,new_x
            else:
                d=(d+1)%4
    matrix[sweeper[num][0]][sweeper[num][1]]=-1

r,c,t=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(r)]
matrix_temp=[[0]*c for _ in range(r)]
direct=[(-1,0),(0,1),(1,0),(0,-1)]
sweeper=[]
cnt=0
isEnd=False
for i in range(r):
    for j in range(c):
        if matrix[i][j]==-1:
            sweeper.append((i,j))
            cnt+=1
            if cnt==2:
                isEnd=True
                break
    if isEnd:
        break

for time in range(t):
    move()
    sweep(sweeper[0][0],sweeper[0][1],1,0)
    sweep(sweeper[1][0],sweeper[1][1],1,1)

result=0
for i in range(r):
    for j in range(c):
        if matrix[i][j]>=1:
            result+=matrix[i][j]
print(result)