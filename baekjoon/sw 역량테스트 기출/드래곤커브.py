import sys
sys.stdin=open("드래곤커브.txt","r")

def count(cnt):
    for i in range(100):
        for j in range(100):
            if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
                cnt+=1
    return cnt

def rotate(Y,X,D):
    temp=[]
    for idx in range(len(visited)-1,-1,-1):
        D=(visited[idx]+1)%4
        Y+=direct[D][0]
        X+=direct[D][1]
        matrix[Y][X]=1
        temp.append(D)
    for idx in range(len(temp)):
        visited.append(temp[idx])
    return Y,X,D

direct=[(0,1),(-1,0),(0,-1),(1,0)]
n=int(input())
matrix=[[0]*101 for _ in range(101)]

for _ in range(n):
    visited = []
    x, y, d, g = map(int, input().split())
    matrix[y][x] = 1
    y += direct[d][0]
    x += direct[d][1]
    matrix[y][x] = 1
    visited.append(d)
    for i in range(g):
        y,x,d=rotate(y,x,d)

result=count(0)
print(result)