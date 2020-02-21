# #with Stack
# import sys
# sys.stdin = open("2468.text","r")

def FindNext(y,x,h):
    for dir in range(len(dy)):
        new_y = y+dy[dir]
        new_x = x+dx[dir]
        if 0<=new_y<len(a) and 0<=new_x<len(a) and a[new_y][new_x]!=-1 and a[new_y][new_x]>h:
            a[new_y][new_x]=-1
            return new_y,new_x
    return -10, -10

def deTect(y,x,h):
    a[y][x] = -1
    stack.append([y,x])

    while stack:
        y,x = FindNext(y,x,h)
        while y!=-10:
            stack.append([y,x])
            y,x = FindNext(y,x,h)
        y, x = stack.pop()
        if not stack:
            y,x = FindNext(y, x, h)
            if y != -10:
                stack.append([y,x])
    return

n = int(input())
matrix=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
M=0
m=987654321
for i in range(n):
    for j in range(n):
        if matrix[i][j] > M:
            M = matrix[i][j]
        
max_val = 0
a=[[0]*n for _ in range(n)]
for h in range(0,M+1):
    stack=[]
    for i in range(n):
        for j in range(n):
            a[i][j] = matrix[i][j] 
    cnt=0
    for y in range(n):
        for x in range(n):
            # for row in a:
            #     print(*row)
            # print()
            if a[y][x]>h and a[y][x]!=-1:
                deTect(y,x,h)
                cnt+=1
    if max_val<cnt:
        max_val = cnt
print(max_val)
