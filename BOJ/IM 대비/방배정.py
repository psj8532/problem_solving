# 방 배정   # 11 : 33
n, k = map(int,input().split())

student = [[0]*2 for i in range(7)]
for t in range(n):
    data = list(map(int,input().split()))
    
    if data[1] == 1:
        if data[0]:
            student[1][1] += 1
        else:
            student[1][0] += 1
    elif data[1] == 2:
        if data[0]:
            student[2][1] += 1
        else:
            student[2][0] += 1
    elif data[1] == 3:
        if data[0]:
            student[3][1] += 1
        else:
            student[3][0] += 1
    elif data[1] == 4:
        if data[0]:
            student[4][1] += 1
        else:
            student[4][0] += 1
    elif data[1] == 5:
        if data[0]:
            student[5][1] += 1
        else:
            student[5][0] += 1
    else:
        if data[0]:
            student[6][1] += 1
        else:
            student[6][0] += 1

cnt = 0
for i in range(1,7):
    for j in range(2):
        if student[i][j]:
            if student[i][j] % k:
                cnt += (student[i][j]//k + 1)
            else:    
                cnt += (student[i][j]//k)

print(cnt)

# 00:37