import sys
sys.stdin = open("경사로.txt","r")

def check_up_x(ty, tx, tl):
    if tx - tl > 0 and Matrix[ty][tx-tl-1] <= Matrix[ty][tx-tl]:
        return True
    elif tx - tl == 0:
        return True
    else:
        return False

def check_up_y(tx, ty, tl):
    if ty - tl > 0 and Matrix[ty-tl-1][tx] <= Matrix[ty-tl][tx]:
        return True
    elif ty - tl == 0:
        return True
    else:
        return False

def check_down_x(ty,tx,tv):
    for j in range(tx+1,tx+L):
        if tx+L<=N and tv == Matrix[ty][j]:
            continue
        else:
            return False
    else:
        if tx+L == N:
            return N-1
        elif tx+L<N:
            if Matrix[ty][tx+L-1] >= Matrix[ty][tx+L]:
                return tx+L-1
        else:
            return False

def check_down_y(tx,ty,tv):
    for j in range(ty+1,ty+L):
        if ty+L<=N and tv == Matrix[j][tx]:
            continue
        else:
            return False
    else:
        if ty+L == N:
            return N-1
        elif ty+L<N:
            if Matrix[ty+L-1][tx] >= Matrix[ty+L][tx]:
                return ty+L-1
        else:
            return False

N,L = map(int,input().split())
Matrix = [list(map(int,input().split())) for _ in range(N)]
road = 0

for y in range(N):
    x = cnt = 1
    val = Matrix[y][0]
    while x!=N:
        if val == Matrix[y][x]:
            cnt += 1
        elif val-Matrix[y][x]==-1 and x==N-1:
            if check_up_x(y,x,L):
                pass
            else:
                break
        elif val-Matrix[y][x]==-1 and cnt>=L:
            if check_up_x(y,x,L):
                cnt,val = 1, Matrix[y][x]
            else:
                break
        elif val-Matrix[y][x]==1:
            x = check_down_x(y,x,Matrix[y][x])
            if x:
                cnt,val = 0,Matrix[y][x]
            else:
                break
        else:
            break
        x += 1
    if x == N:
        road += 1
        print('{} right'.format(y))

for x in range(N):
    y = cnt = 1
    val = Matrix[0][x]
    while y!=N:
        if val == Matrix[y][x]:
            cnt += 1
        elif val-Matrix[y][x]==-1 and y==N-1:
            if check_up_y(x,y,L):
                pass
            else:
                break
        elif val-Matrix[y][x]==-1 and cnt>=L:
            if check_up_y(x, y, L):
                cnt,val = 1, Matrix[y][x]
            else:
                break
        elif val-Matrix[y][x]==1:
            y = check_down_y(x,y,Matrix[y][x])
            if y:
                cnt,val = 0,Matrix[y][x]
            else:
                break
        else:
            break
        y += 1
    if y == N:
        road += 1
        print('{} down'.format(x))

print(road)