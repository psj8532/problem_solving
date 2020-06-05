import sys
sys.stdin=open("스티커붙이기.txt","r")

n,m,k=map(int,input().split()) #세로, 가로, 스티커 갯수
matrix=[[0]*m for _ in range(n)]

for _ in range(k):
    R,C = map(int,input().split())
    data=[list(map(int,input().split())) for i in range(R)]
    y,x=R,C
    visited=[]
    for cnt in range(4):
        isNext=False
        for i in range(n-y+1):
            for j in range(m-x+1):
                isNext=False
                for r in range(i,i+y):
                    for c in range(j,j+x):
                        isFail = False
                        if not matrix[r][c] and data[r-i][c-j]:
                            visited.append((r, c, matrix[r][c]))
                            matrix[r][c]=data[r-i][c-j]
                        elif not matrix[r][c] and not data[r-i][c-j]:
                            pass
                        elif matrix[r][c] and not data[r-i][c-j]:
                            pass
                        elif matrix[r][c] and data[r-i][c-j]:
                            isFail=True#회전 전 찾기 실패
                            while visited:
                                posi_y,posi_x,temp=visited.pop()
                                matrix[posi_y][posi_x]=temp
                            break
                    if isFail:
                        break
                else:#붙일 곳 찾음
                    isNext=True
                    break
            if isNext:
                break
        else:#못찾았으면 회전
            if not isNext:
                data_temp=[[0]*y for __ in range(x)]
                for i in range(y):
                    idx=y-1-i
                    for j in range(x):
                        data_temp[j][idx]=data[i][j]
                y, x = x, y
                data=[[0]*x for __ in range(y)]
                for i in range(y):
                    for j in range(x):
                        data[i][j]=data_temp[i][j]
        if isNext:
            break
count=0
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            count+=1
print(count)