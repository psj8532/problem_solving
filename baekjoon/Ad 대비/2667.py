#단지번호 붙이기 #21:00
import sys
sys.stdin = open("2667.text","r")
# for문으로 1인 곳 탐지 -> 그 곳부터 델타를 이용하여 1인 곳 번호 매겨가기
# 하나의 단지가 탐지 완료되면 단지내 집의 수를 리스트에 추가
#  다른 1 탐지

def complex(y,x):
    global cnt
    matrix[y][x]=0
    for dir in range(len(dy)):
        new_y = y+dy[dir]
        new_x = x+dx[dir]
        if 0<=new_y<n and 0<=new_x<n and matrix[new_y][new_x]==1:
            matrix[new_y][new_x]=0
            cnt+=1
            complex(new_y,new_x)
    return cnt

n=int(input())
matrix=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
result = []
for _ in range(n):
    matrix.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            cnt=1
            temp = complex(i,j)
            result.append(temp)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
#21:27