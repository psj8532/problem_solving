#9663 #9:59
import sys
sys.stdin = open("N_Queen.text","r")
#DFS로 탐색하면서
#가로,세로,대각선에 퀸이 있으면 백
#for문으로 [0]행의 열들을 확인
#nextFind를 통해 다음 행에서의 열 찾음
#check함수를 통해 가로,세로,대각선을 확인하고 안되면 백
#끝가지 가면 cnt+1

def backTracking(row,b):
    if row==n:
        global cnt
        cnt+=1
        return
    visited[b]=1
    for x in range(n):
        if not visited[x] and (x<b-1 or x>b+1):
            b = x
            backTracking(row+1,b)
            visited[b]=0
    return
n=int(input())
matrix = [[0]*n for _ in range(n)]

cnt=0
for i in range(n):
    visited = [0] * n
    backTracking(0,i)
print(cnt)



# #재귀
# def isCheck(y,x):
#     for i in range(y):
#         if (y!=i and matrix[i][x]):
#             return False
#     for dir in range(len(dy)):
#         new_y=y+dy[dir]
#         new_x=x+dx[dir]
#         while 0<=new_y<n and 0<=new_x<n:
#             if matrix[new_y][new_x]:
#                 return False
#             new_y+=dy[dir]
#             new_x+=dx[dir]
#     return True
#
# def dfs(here):
#     if here == n:
#         global cnt
#         cnt+=1
#         return
#     for x in range(n):
#         matrix[here][x]=1
#         if isCheck(here,x):
#             dfs(here+1)
#         matrix[here][x]=0
#         if here==0 and x==n//2-1:
#             return
#     return
#
# dy=[-1,-1]
# dx=[1,-1]
#
# n=int(input())
# matrix = [[0]*n for _ in range(n)]
# cnt=0
# dfs(0)
# print(cnt*2)