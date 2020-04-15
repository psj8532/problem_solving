import sys
sys.stdin = open("경사로.txt","r")

def check_up(y,x,l):
    if x-l==0:
        return True
    elif x-l>0 and matrix[y][x-l-1]<=matrix[y][x-l]:
        return True
    else:
        return False

def check_down(y,x,v):
    for j in range(x+1,x+L):
        if x+L<N and matrix[y][j] == v:
            continue
        else:
            return False
    else:
        if x+L == N:
            return N-1
        elif x+L < N-1 and matrix[y][x+L-1] >= matrix[y][x+L]:
            return x+L-1
        else:
            return False

N,L = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
matrix_rotate = [[0]*N for _ in range(N)]
road = 0

for r in range(N):
    c = cnt = 1
    val = matrix[r][0]
    while c!=N:
        if matrix[r][c] == val:
            cnt += 1
        elif val-matrix[r][c]==-1 and c==N-1:
            if check_up(r,c,L):
                pass
            else:
                break
        elif val-matrix[r][c]==-1 and cnt>=L:
            if check_up(r,c,L):
                cnt,val = 1,matrix[r][c]
            else:
                break
        elif val-matrix[r][c]==1:
            c = check_down(r,c,matrix[r][c])
            if c:
                cnt,val = 0, matrix[r][c]
            else:
                break
        else:
            break
        c += 1
    if c == N:
        road += 1

for i in range(N):
    for j in range(N):
        matrix_rotate[j][i] = matrix[i][j]

for i in range(N):
    for j in range(N):
        matrix[i][j] = matrix_rotate[i][j]

for r in range(N):
    c = cnt =1
    val = matrix[r][0]
    while c!=N:
        if matrix[r][c] == val:
            cnt += 1
        elif val-matrix[r][c]==-1 and c==N-1:
            if check_up(r,c,L):
                pass
            else:
                break
        elif val-matrix[r][c]==-1 and cnt>=L:
            if check_up(r,c,L):
                cnt,val = 1,matrix[r][c]
            else:
                break
        elif val-matrix[r][c]==1:
            c = check_down(r,c,matrix[r][c])
            if c:
                cnt,val = 0, matrix[r][c]
            else:
                break
        else:
            break
        c += 1
    if c == N:
        road += 1

print(road)