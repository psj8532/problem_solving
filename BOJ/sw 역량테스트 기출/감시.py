def count(c,matrix_temp): #리스트를 여러곳에서 쓸거면 인자로 넘길것
    for i in range(N):
        for j in range(M):
            if not matrix_temp[i][j]:
                c += 1
    return c

def copy(s):
    a = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            a[i][j] = s[i][j]
    return a

def detect(y,x,d,matrix_temp):
    new_y, new_x = y + direct[d][0], x + direct[d][1]
    while 0 <= new_y < N and 0 <= new_x < M and matrix_temp[new_y][new_x] != 6:
        if not matrix_temp[new_y][new_x]:
            matrix_temp[new_y][new_x] = -1
        new_y, new_x = new_y+direct[d][0], new_x + direct[d][1]

def cctv_check(y,x,num,d,matrix_temp):
    if num==1:
        detect(y,x,d,matrix_temp)
    elif num==2 or num==3:
        if num==2:
            temp_d1 = d2[d][0]
            temp_d2 = d2[d][1]
        else:
            temp_d1 = d3[d][0]
            temp_d2 = d3[d][1]
        detect(y,x,temp_d1,matrix_temp)
        detect(y,x,temp_d2,matrix_temp)
    elif num==4:
        temp_d1 = d4[d][0]
        temp_d2 = d4[d][1]
        temp_d3 = d4[d][2]
        detect(y,x,temp_d1,matrix_temp)
        detect(y,x,temp_d2,matrix_temp)
        detect(y,x,temp_d3,matrix_temp)
    else:
        for idx in range(4):
            detect(y,x,idx,matrix_temp)

def observe(index,matrix_temp):
    global min
    if index==len(cctv_list):
        cnt = count(0,matrix_temp)
        if cnt < min:
            min = cnt
        return

    for i in range(cctv[cctv_list[index][2]]):
        s = copy(matrix_temp)
        cctv_check(cctv_list[index][0],cctv_list[index][1],cctv_list[index][2],i,matrix_temp) #탐지
        observe(index+1,matrix_temp) #다음카메라로
        matrix_temp = copy(s)

N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
cctv_list = []
matrix_temp = copy(matrix)
cctv = [0,4,2,4,4,1]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
d2 = [(0,2),(1,3)]
d3 = [(0,1),(1,2),(2,3),(3,0)]
d4 = [(0,1,2),(1,2,3),(2,3,0),(3,0,1)]
min = 9876543210
for i in range(N):
    for j in range(M):
        if 1<=matrix_temp[i][j]<=5:
            cctv_list.append([i, j, matrix_temp[i][j]])

observe(0,matrix_temp)
print(min)