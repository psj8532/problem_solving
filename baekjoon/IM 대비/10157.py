#자리배정   #18:45
import sys
sys.stdin = open("10157.text","r")

def Doturn(y, x, w, h):
    if y<0 or y>=h or x<0 or x>=w or matrix[y][x] != 0:
        return True
    else:
        return False

w, h = map(int,input().split())

matrix = [[0]*w for _ in range(h)]

n = int(input())
num = list(range(1,w*h+1))

dy=[1, 0, -1, 0]
dx=[0, 1, 0, -1]
dir = 0
k=0
y=0
x=0
for i in range(w*h):  
    if k<=len(num):
        matrix[y][x]=num[k]
        new_y = y + dy[dir]
        new_x = x + dx[dir]
        k+=1
        if Doturn(new_y, new_x, w, h):
            dir+=1
            dir %= len(dy)
            y += dy[dir]
            x += dx[dir]
        else:
            y = new_y
            x = new_x

IsEnd = False
for i in range(h):
    for j in range(w):
        if matrix[i][j]==n:
            print('{} {}'.format(j+1, i+1))
            IsEnd = True
            break
            
if IsEnd == False:
    print(0)