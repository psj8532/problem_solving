#20:00 #스도쿠
import sys
sys.stdin = open("2580.text")

def position_y(y):
    if 0 <= y < 3:
        a = range(0,3)
    elif 3 <= y < 6:
        a = range(3,6)
    elif 6 <= y < 9:
        a = range(6,9)
    return a

def position_x(x):
    if 0 <= x < 3:
        b = range(0,3)
    elif 3 <= x < 6:
        b = range(3,6)
    elif 6 <= x < 9:
        b = range(6,9)
    return b

def check(y,x,num):
    for i in range(9):
        if y!=i and matrix[i][x] == num:
            return False
    for j in range(9):
        if x!=j and matrix[y][j] == num:
            return False
    a = position_y(y)
    b = position_x(x)
    for i in a:
        for j in b:
            if (y,x)!=(i,j) and matrix[i][j] == num:
                return False
    return True

def play(y,x,num):
    matrix[y][x]=num
    if y == 8 and x == 8:
        global ans
        for row in matrix:
            print(*row)
        ans = 1
        return
    else:
        i=y
        j=x+1
        if j>=9:
            j=0
            i+=1
        while i<9:
            if not matrix[i][j]:
                for next_num in range(1,10):
                    if check(i,j,next_num):
                        play(i,j,next_num)
                        if ans:
                            return
                else:
                    matrix[y][x]=0
                    return
            j += 1
            if j == 9:
                i += 1
                j = 0

matrix = []
for _ in range(9):
    matrix.append(list(map(int,input().split())))
ans = 0
y=x=0
while y<9:
    if not matrix[y][x]:
        for num in range(1, 10):
            if check(y,x,num):
                play(y,x,num)
            if ans:
                break
    if ans:
        break
    x+=1
    if x==9:
        y+=1
        x=0

#23:39 #시간 초과
