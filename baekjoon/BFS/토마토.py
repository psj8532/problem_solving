#7576 #15:23 #백트래킹 사용할것
import sys
sys.stdin=open("토마토.text","r")

def bfs(max_val):
    global count
    while queue:
        here = queue.pop(0)
        y = here[0]
        x = here[1]
        depth=here[2]
        if depth>max_val:
            max_val=depth
        for dir in range(len(dy)):
            temp_y = y + dy[dir]
            temp_x = x + dx[dir]
            if 0 <= temp_y < n and 0 <= temp_x <m and matrix[temp_y][temp_x] == 0:
                queue.append([temp_y, temp_x, depth + 1])
                matrix[temp_y][temp_x] = 1
                count-=1
    return max_val
dy=[-1,0,1,0]
dx=[0,1,0,-1]
m,n=map(int,input().split())
matrix=[]
queue=[]
temp=0
max_val=0
count=0
for _ in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            queue.append([i,j,0])
        elif matrix[i][j]==0:
            count+=1
cnt = bfs(max_val)

# for row in matrix:
#     if not all(row):
#         temp=-1
#         break

# for i in range(n):
#     for j in range(m):
#         if matrix[i][j]==0:
#             temp=-1
#             break
#     if temp==-1:
#         break

if count>0:
    print(-1)
else:
    print(cnt)