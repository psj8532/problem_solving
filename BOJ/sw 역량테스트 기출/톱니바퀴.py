def rotate(idx,d):
    if rot[idx]:
        if d==1:
            temp=matrix[idx][7]
            matrix_temp=matrix[idx][0:7]
            matrix[idx][0]=temp
            for j in range(1,8):
                matrix[idx][j]=matrix_temp[j-1]
        elif d==-1:
            temp=matrix[idx][0]
            matrix_temp=matrix[idx][1:8]
            matrix_temp.append(temp)
            for j in range(8):
                matrix[idx][j]=matrix_temp[j]

matrix=[list(map(int,input())) for _ in range(4)]
k=int(input())

for _ in range(k):
    s,dir=map(int,input().split())
    s-=1
    dir_temp,temp_s=dir,s
    rot=[0]*4
    rot[temp_s]=dir_temp
    while temp_s<3 and matrix[temp_s][2]!=matrix[temp_s+1][6]:
        temp_s+=1
        dir_temp=-dir_temp
        rot[temp_s]=dir_temp
    dir_temp,temp_s=dir,s
    while 0<temp_s and matrix[temp_s-1][2]!=matrix[temp_s][6]:
        temp_s-=1
        dir_temp=-dir_temp
        rot[temp_s]=dir_temp
    for i in range(4):
        rotate(i,rot[i])
result=0
for i in range(4):
    if matrix[i][0]:
        if i == 0:
            result += 1
        elif i == 1:
            result += 2
        elif i == 2:
            result += 4
        elif i == 3:
            result += 8
print(result)
#1:17