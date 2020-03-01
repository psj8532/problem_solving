#9663 #9:59
import sys
sys.stdin = open("N_Queen.text","r")

def backTrack(row,b):
    visited_col[b]=1
    visited_l[matrix_l[row][b]]=1
    visited_r[matrix_r[row][b]]=1
    if row == n-1:
        global cnt
        cnt+=1
        return
    for x in range(n):
        if not visited_col[x] and not visited_l[matrix_l[row+1][x]] and not visited_r[matrix_r[row+1][x]]:
            backTrack(row+1,x)
            visited_col[x]=0
            visited_l[matrix_l[row + 1][x]]=0
            visited_r[matrix_r[row + 1][x]]=0

n=int(input())
cnt=0
matrix_l=[[0]*n for _ in range(n)]
matrix_r=[[0]*n for _ in range(n)]
temp=3
for i in range(n):
    t=temp+1
    for j in range(n):
        t-=1
        matrix_l[i][j]=t
    temp+=1
temp=-2
for i in range(n):
    t=temp+1
    for j in range(n):
        t+=1
        matrix_r[i][j]=t
    temp+=1

for i in range(n // 2):
    visited_col = [0]*n
    visited_l = [0]*(2*n)
    visited_r = [0]*(2*n)
    backTrack(0,i)
cnt *= 2
if n>1 and n&1:
    visited_col = [0] * n
    visited_l = [0] * (2 * n)
    visited_r = [0] * (2 * n)
    backTrack(0, n // 2)
elif n==1:
    cnt+=1
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