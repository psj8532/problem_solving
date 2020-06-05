from collections import deque

def bfs():
    global count
    while deq:
        here = deq.popleft()
        y = here[0]
        x = here[1]
        depth=here[2]

        for dir in range(len(dy)):
            temp_y = y + dy[dir]
            temp_x = x + dx[dir]
            if 0 <= temp_y < n and 0 <= temp_x <m and not matrix[temp_y][temp_x]:
                deq.append([temp_y, temp_x, depth + 1])
                matrix[temp_y][temp_x] = 1
                count-=1
    return depth

dy=[-1,0,1,0]
dx=[0,1,0,-1]
m,n=map(int,input().split())
matrix=[]
deq=deque()
temp=0
max_val=0
count=0
for _ in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            deq.append([i,j,0])
        elif matrix[i][j]==0:
            count+=1
cnt = bfs()

if count>0:
    print(-1)
else:
    print(cnt)