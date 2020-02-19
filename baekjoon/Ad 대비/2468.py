#12:18 #안전 영역
import sys
sys.stdin = open("2468.text","r")

# 높이1~최대일때까지 for문으로 반복
# 기준 높이 이하의 지점을 찾으면 0으로 바꾸고 높이가 바뀌면 다시 탐색
# 함수가 끝날때 cnt++
# 메인함수의 함수 호출 완료 후 갯수 셈
def deTect(y,x,h):
    for dir in range(len(dy)):
        new_y = y+dy[dir]
        new_x = x+dx[dir]
        if 0<=new_y<n and 0<=new_x<n and a[new_y][new_x]-h>0:
            a[new_y][new_x]+=h
            deTect(new_y,new_x,h)
    return
n = int(input())
matrix=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
max_val = 0
for h in range(1,101):
    a = matrix[:]
    cnt=0
    for y in range(n):
        for x in range(n):
            if a[y][x]>h:
                deTect(y,x,h)
                cnt+=1
    if max_val<cnt:
        max_val = cnt
    if cnt==0:
        break
print(cnt)