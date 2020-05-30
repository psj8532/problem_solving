import sys
sys.stdin = open("스도쿠.txt", "r")
import time

stime = time.time()

def check_row(y,x): #행 검사
    for j in range(9):
        if j != x and sudo[y][j] == sudo[y][x]:
            return False
    return True


def check_col(y,x): #열 검사
    for i in range(9):
        if i != y and sudo[i][x] == sudo[y][x]:
            return False
    return True


def check_rect(y,x): # 3x3영역 안 검사하기
    sy, sx = 3 * (y // 3), 3 * (x // 3)
    y, x = 3 * (y // 3) + (y % 3), 3 * (x // 3) + (x % 3)
    for i in range(sy, sy + 3):
        for j in range(sx, sx + 3):
            if (i,j)!=(y,x) and sudo[i][j] == sudo[y][x]:
                return False
    return True


def dfs(index):
    global isSuccess
    if index == n:
        isSuccess = True
        for row in sudo:
            print(*row)
        return

    y, x = cand[index][0], cand[index][1]
    for num in range(1,10):
        sudo[y][x] = num
        if not check_row(y,x) or not check_col(y,x) or not check_rect(y,x):
            continue
        dfs(index+1)
        if isSuccess:
            return
    else:
        sudo[y][x] = 0


sudo = [list(map(int,input().split())) for _ in range(9)]
isSuccess = False
cand = []
for i in range(9):
    for j in range(9):
        if not sudo[i][j]:
            cand.append((i,j))
n = len(cand)
dfs(0)
print('time: {}'.format(time.time()-stime))