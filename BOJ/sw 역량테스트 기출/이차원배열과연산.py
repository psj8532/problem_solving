def check():
    if r >= R or c >= C:
        return False
    elif matrix[r][c] == k:
        return True
    else:
        return False

def my_sort(isCheck,y,x):
    for i in range(R):
        a = []
        m = max(matrix[i])
        counting = dict()
        c = [0] * (m+1)
        for j in range(y):
            c[matrix[i][j]] += 1
        cnt = max(c)
        idx = c.index(x)
        if not cnt: continue
        if not counting[cnt]:
            counting[cnt] = idx
        else:
            counting[cnt] += idx
        while counting:
            key_min = min(counting.keys())
            a.append(counting[key_min])
            a.append(key_min)
            temp = a[:]
            newMatrix.append(temp)
            del counting[key_min]

r,c,k = map(int,input())
matrix = [list(map(int,input().split())) for _ in range(3)]
time = 0
R = C = 3
while time < 100:
    newMatrix = []
    if check():
        print(time)
    else:
        if R >= C:
            my_sort(1,R,C) # 행
        else:
            my_sort(2,C,R) # 열

    time += 1