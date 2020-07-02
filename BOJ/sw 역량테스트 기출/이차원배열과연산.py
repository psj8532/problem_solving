def check():
    if r >= R or c >= C:
        return False
    elif matrix[r][c] == k:
        return True
    else:
        return False

def my_sort(isCheck,y,x):
    max = 0
    for i in range(y):
        a = []
        m = max(matrix[i])
        counting = dict()
        c = [0] * (m+1)
        for j in range(y):
            c[matrix[i][j]] += 1
        cnt = max(c)
        idx = c.index(cnt)
        if not cnt or not idx: continue
        if not counting[cnt]:
            counting[cnt] = idx
        else:
            counting[cnt] += idx
        cnt = 0
        while counting and cnt < 100:
            key_min = min(counting.keys())
            a.append(counting[key_min])
            a.append(key_min)
            temp = a[:]
            newMatrix.append(temp)
            del counting[key_min]
            cnt += 2
        if cnt > max:
            max = cnt

    for i in range(y):
        

r,c,k = map(int,input())
matrix = [list(map(int,input().split())) for _ in range(3)]
time = 0
while time < 100:
    newMatrix = []
    R = len(matrix)
    C = len(matrix[0])
    if check():
        print(time)
    else:
        if R >= C:
            my_sort(1,R,C) # 행
        else:
            my_sort(2,C,R) # 열

        time += 1

