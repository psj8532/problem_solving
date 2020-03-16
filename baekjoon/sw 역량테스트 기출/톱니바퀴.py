#10:50
#[2]와 [6]비교
#시계방향 회전은 [7],[0]~[6]
#반시계방향 회전은 [1]~[7],[0]
#회전했고 [2],[6]이 서로 다르다면 반대방향으로 회전
import sys
sys.stdin=open("톱니바퀴.text")

def move(idx,d):
    if d==1:
        temp=matrix[idx][7]
        matrix_temp=matrix[idx][0:7]
        matrix[0]=temp
        for j in range(1,8):
            matrix[idx][j]=matrix_temp[j-1]
    else:
        temp=matrix[idx][0]
        matrix_temp=matrix[idx][1:8]
        matrix_temp.append(temp)
        for j in range(8):
            matrix[idx][j]=matrix_temp[idx][j]

def rotate():
    for i in range(4):
        if diff[i] and rot[i]:
            move(i,rot[i])

matrix=[list(map(int,input())) for _ in range(4)]
k=int(input())#회전횟수

for _ in range(k):
    diff = [0] * 4
    rot = [0]*4
    s,dir=map(int,input().split())
    rot[s]=dir
    for i in range(3):
        if matrix[i][2]==matrix[i+1][6]:
            diff[i]=diff[i+1]=1
    if matrix[2][6]==matrix[3][6] #diff정보는 회전한 방향에 따ㅏ 다라짐
    temp_s=s
    while temp_s<3:
        temp_s+=1
        if rot[temp_s-1]:
            if rot[temp_s-1]==1:
                rot[temp_s]=-1
            else:
                rot[temp_s]=1
    temp_s=s
    while temp_s>0:
        temp_s-=1
        if rot[temp_s+1]:
            rot[temp_s]=1

    rotate()
result=0
for i in range(4):
    if matrix[i][0]:
        if i == 0:
            result += 1
        elif i == 1:
            result += 2
        elif i == 1:
            result += 4
        elif i == 1:
            result += 8
print(result)