#1987 #15:04
#출발지점의 cnt=1로 초기화
#도착할 곳의 조건은 비지티드가 표시되어 있지 않고, 리스트에도 없어야함
#자기가 도착한 곳의 알파벳을 추가하고 비지티드에도 표시,cnt+=1
#r:세로,c:가로
#비지티드 2차원, 매트릭스 2차원
#max값 비교

import sys
sys.stdin = open("알파벳.text","r")
# DFS
def dfs(y,x,cnt):
    isEnd=False
    global max_cnt
    cnt+=1
    visit_list[ord(matrix[y][x])-65]=1
    if max_cnt<cnt:
        max_cnt=cnt
        if max_cnt==26:
            isEnd=True
            return

    for dir in range(len(dy)):
        new_y=y+dy[dir]
        new_x=x+dx[dir]
        if 0<=new_y<r and 0<=new_x<c and not visit_list[ord(matrix[new_y][new_x])-65]:
            dfs(new_y,new_x,cnt)
            if isEnd:
                return
            visit_list[ord(matrix[new_y][new_x])-65]=0

r,c = map(int,input().split())
matrix=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for _ in range(r):
    matrix.append(list(input()))
visit_list=[0]*26
max_cnt=0
dfs(0,0,0)
print(max_cnt)
#20:01
