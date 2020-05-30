import sys
sys.stdin = open("쿼드트리.txt", "r")

def check(sy,ey,sx,ex):
    for i in range(sy,ey):
        for j in range(sx, ex):
            if matrix[i][j] != matrix[sy][sx]:
                return False
    return True


def movie(sy,ey,sx,ex,m):
    if check(sy,ey,sx,ex):
        print(matrix[sy][sx], end='')
    else:
        mid = m>>1
        print('(', end='')
        movie(sy, sy + mid, sx, sx + mid, mid)
        movie(sy, sy + mid, sx + mid, ex, mid)
        movie(sy + mid, ey, sx, sx + mid, mid)
        movie(sy + mid, ey, sx + mid, ex, mid)
        print(')', end='')


N = int(input())
matrix = [list(map(int,input())) for _ in range(N)]
movie(0,N,0,N,N)