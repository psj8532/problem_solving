#3190 #22:25
#처음 뱀의 이동방향은 오른쪽
#뱀의 방향 정보는 data 리스트에 저장 #data[1]에 따라 방향 전환
#visited에 표시하면서 이동하며, 사과가 있을시 visited 유지, 없다면 끝에거 취소
import sys
sys.stdin=open("뱀.text","r")

n=int(input())#보드의 크기
k=int(input())#사과의 갯수
matrix=[[0]*n for _ in range(n)] #맵
for i in range(k):
    y,x=map(int,input().split())
    matrix[y-1][x-1]=1
for row in matrix:
    print(*row)
d=int(input())
data=[list(map(str,input().split())) for _ in range(d)] #방향 정보
for i in range(d):
    data[i][0] = int(data[i][0])
