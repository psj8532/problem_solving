#12:18 #안전 영역 #재귀 너무 많이 호출되어 런타임 에러 발생
#with Recursion
import sys
sys.stdin = open("2468.text","r")
sys.setrecursionlimit(10**6)

# 높이1~최대일때까지 for문으로 반복
# 기준 높이 이하의 지점을 찾으면 0으로 바꾸고 높이가 바뀌면 다시 탐색
# 함수가 끝날때 cnt++
# 메인함수의 함수 호출 완료 후 갯수 셈
def deTect(y,x,n,h):
    for dir in range(len(dy)):
        new_y = y+dy[dir]
        new_x = x+dx[dir]
        if 0<=new_y<n and 0<=new_x<n and a[new_y][new_x]!=-1 and a[new_y][new_x]-h>0:
            a[new_y][new_x]=-1
            deTect(new_y,new_x,n,h)
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
            M= matrix[i][j]
        
max_val = 0
a=[[0]*n for _ in range(n)]
for h in range(0,M+1):
    for i in range(n):
        for j in range(n):
            a[i][j] = matrix[i][j] 
    cnt=0
    for y in range(n):
        for x in range(n):
            if a[y][x]>h and a[y][x]!=0:
                a[y][x]=-1
                deTect(y,x,n,h)
                cnt+=1
    if max_val<cnt:
        max_val = cnt
        posi=h
print(max_val,posi)