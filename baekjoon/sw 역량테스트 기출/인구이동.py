import sys
sys.stdin=open("인구이동.txt")
from collections import deque

def bfs(y,x):
    global isfail
    deq = deque()
    union = []
    deq.append((y,x))
    union.append((y,x))
    visited[y][x] = 1
    sum = matrix[y][x]

    while deq:
        here = deq.popleft()
        y,x = here[0],here[1]
        for dir in range(len(direct)):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<N and not visited[new_y][new_x] and L<=abs(matrix[new_y][new_x]-matrix[y][x])<=R :
                union.append((new_y,new_x))
                deq.append((new_y,new_x))
                visited[new_y][new_x] = 1
                sum += matrix[new_y][new_x]
                isfail = False

    if len(union)>1:
        val = sum//len(union)
        for i in range(len(union)):
            matrix_temp[union[i][0]][union[i][1]] = val

direct=[(-1,0),(0,1),(1,0),(0,-1)]
N,L,R = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
count = 0
isfail = False

while not isfail:
    isfail = True
    visited = [[0] * N for _ in range(N)]
    matrix_temp = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j)

    if not isfail:
        count+=1
        for i in range(N):
            for j in range(N):
                if matrix_temp[i][j]!=-1:
                    matrix[i][j] = matrix_temp[i][j]
print(count)
#인구 이동이 일어날 때마다 count+1 해줬는데 인구이동한 일수를 세는 문제였음

# def bfs(y,x):
#     deq = deque()
#     visited = [[0]*N for _ in range(N)]
#     deq.append((y,x))
#     visited[y][x] = 1
#     union[y][x] = 0
#     union_list.append((y,x))
#     s = matrix[y][x]
#
#     while deq:
#         here = deq.popleft()
#         y,x = here[0],here[1]
#         for dir in range(len(direct)):
#             new_y,new_x = y+direct[dir][0],x+direct[dir][1]
#             if 0<=new_y<N and 0<=new_x<N and union[new_y][new_x] and not visited[new_y][new_x]:
#                 deq.append((new_y,new_x))
#                 visited[new_y][new_x] = 1
#                 union_list.append((new_y,new_x))
#                 s += matrix[new_y][new_x]
#                 union[new_y][new_x] = 0
#     return s

# union = [[0]*N for _ in range(N)]
# count = 0
# for i in range(N):
#     for j in range(N-1):
#         if L<=abs(matrix[i][j]-matrix[i][j+1])<=R:
#             union[i][j]=union[i][j+1]=1
# for j in range(N):
#     for i in range(N-1):
#         if L<=abs(matrix[i][j]-matrix[i+1][j])<=R:
#             union[i][j]=union[i+1][j]=1
# for i in range(N):
#     for j in range(N):
#         union_list = []
#         if union[i][j]:
#             sum=0
#             sum += bfs(i,j)
#             count += 1
#             people = sum//len(union_list)
#         if union_list:
#             for r in range(len(union_list)):
#                 y,x = union_list[r][0],union_list[r][1]
#                 matrix[y][x] = people
# print(count)