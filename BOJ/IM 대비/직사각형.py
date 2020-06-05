# 직사각형 # 20:40
import sys
sys.stdin = open("직사각형.txt","r")

for test_case in range(1,5):
    data = list(map(int,input().split()))
    max_val = max(data)
    matrix = [[0]*(max_val+1) for _ in range(max_val+1)]
    for y in range(data[1],data[3]+1):
        for x in range(data[0],data[2]+1):
            matrix[y][x] += 1
    for y in range(data[5],data[7]+1):
        for x in range(data[4],data[6]+1):
            matrix[y][x] += 1
    #검사
    dy =[1,1,0,-1,-1,-1,0,1] 
    dx =[0,1,1,1,0,-1,-1,-1]
    IsEnd = False
    count=0
    for y in range(1,max_val):
        for x in range(1,max_val):
            if matrix[y][x] == 2:
                for dir in range(len(dy)):
                    if matrix[y+dy[dir]][x+dx[dir]]==2:
                        count+=1
                IsEnd =True
                break
        if IsEnd:
            break
    else:
        print('d')
    if IsEnd:
        if count >= 3: #직사각형
            print('a')
        elif count == 2 or count == 1: #선분
            print('b')
        elif count == 0:#점
            print('c')
#21:48 #메모리초과