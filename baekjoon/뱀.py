#3190 #22:25
#처음 뱀의 이동방향은 오른쪽
#뱀의 방향 정보는 data 리스트에 저장 #data[1]에 따라 방향 전환
#visited에 표시하면서 이동하며, 사과가 있을시 visited 유지, 없다면 끝에거 취소
import sys
sys.stdin=open("뱀.text","r")

n=int(input())#보드의 크기
k=int(input())#사과의 갯수
matrix=[[0]*n for _ in range(n)]
for i in range(k):
