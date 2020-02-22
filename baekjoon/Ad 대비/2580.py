#20:00 #스도쿠
import sys
sys.stdin = open("2580.text")

def position_y(y):
    if 0<=y<3:
        a=list(range(0,3))
    elif 3<=y<6:
        a = list(range(3,6))
    elif 6<=y<9:
        a = list(range(6,9))
    return a

def position_x(x):
    if 0 <= x < 3:
        b = list(range(0,3))
    elif 3 <= x < 6:
        b = list(range(3,6))
    elif 6 <= x < 9:
        b = list(range(6,9))
    return b

def check(y,x,num):
    for i in range(9):
        if (y,x)!=(i,x) and matrix[i][x]==num:
            return False
    for j in range(9):
        if (y,x) != (i,x) and matrix[y][j] == num:
            return False
    a = position_y(y)
    b = position_x(x)
    for i in a: # 중복 값이 들어가버림
        for j in b:
            if (y,x)!=(i,j) and matrix[i][j] == num:
                return False
    return True

def play(y,x,num):
    matrix[y][x]=num
    if y == 8 and x == 8:
        global ans
        for _ in range(9):
            print(*matrix[_])
        ans = 1
        return
    else:
        for i in range(9):
            for j in range(9):
                if not matrix[i][j]:
                    for next_num in range(1,10):
                        if check(i,j,next_num):
                            play(i,j,next_num)
                            if ans:
                                return
                    matrix[y][x]=0
                    return

matrix = []
for _ in range(9):
    matrix.append(list(map(int,input().split())))
num_list = list(range(1,10))
IsEnd = False
ans = 0
for y in range(9):
    for x in range(9):
        if not matrix[y][x]:
            for num in range(1, 10):
                if check(y,x,num):
                    play(y,x,num)
                if ans:
                    IsEnd = True
                    break
            IsEnd =True
        if IsEnd:
            break
    if IsEnd:
        break
#23:39 #시간 초과