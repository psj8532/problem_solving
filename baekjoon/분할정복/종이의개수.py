import sys
sys.stdin = open("종이의개수.txt", "r")
import math

def check(sy,ey,sx,ex):
    for i in range(sy,ey):
        for j in range(sx,ex):
            if paper[sy][sx] != paper[i][j]:
                return False
    return True

def div(sy,ey,sx,ex,n):
    if check(sy,ey,sx,ex):
        val = paper[sy][sx]
        if val == -1:
            result[0] += 1
        elif val == 0:
            result[1] += 1
        else:
            result[2] += 1
    else:
        mid1 = int(math.sqrt(n))
        mid2 = mid1*2
        div(sy, sy+mid1, sx, sx+mid1, mid1)
        div(sy, sy+mid1, sx+mid1, sx+mid2, mid1)
        div(sy, sy+mid1, sx+mid2, ex, mid1)

        div(sy+mid1, sy+mid2, sx, sx+mid1, mid1)
        div(sy+mid1, sy+mid2, sx+mid1, sx+mid2, mid1)
        div(sy+mid1, sy+mid2, sx+mid2, ex, mid1)

        div(sy+mid2, ey, sx, sx+mid1, mid1)
        div(sy+mid2, ey, sx+mid1, sx+mid2, mid1)
        div(sy+mid2, ey, sx+mid2, ex, mid1)


N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
result = [0]*3
div(0,N,0,N,N)
for val in result:
    print(val)