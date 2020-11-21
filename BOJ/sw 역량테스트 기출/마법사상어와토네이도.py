import math

def move(y,x,d,ans):
    total = 0
    for dir in range(9):
        ny, nx = y + dy[d][dir], x + dx[d][dir]
        # 1%
        if dir == 0 or dir == 1:
            sand = math.floor(links[y][x] * 0.01)
        # 2%
        elif dir == 2 or dir == 3:
            sand = math.floor(links[y][x] * 0.02)
        # 7%
        elif dir == 4 or dir == 5:
            sand = math.floor(links[y][x] * 0.07)
        # 10%
        elif dir == 6 or dir == 7:
            sand = math.floor(links[y][x] * 0.1)
        # 5%
        else:
            sand = math.floor(links[y][x] * 0.05)

        if 0 <= ny < N and 0 <= nx < N:
            links[ny][nx] += sand
        else:
            ans += sand
        total += sand
    # 나머지
    ny, nx = y + dy[d][9], x + dx[d][9]
    links[y][x] -= total
    if 0 <= ny < N and 0 <= nx < N:
        links[ny][nx] += links[y][x]
    else:
        ans += links[y][x]
    links[y][x] = 0

    return ans


def tornado(by,bx,bd):
    nd = (bd+1) % 4
    ny,nx = by+direct[nd][0],bx+direct[nd][1]
    if visited[ny][nx]:
        ny,nx,nd = by+direct[bd][0],bx+direct[bd][1],bd
        visited[ny][nx] = True
        return ny,nx,nd
    else:
        visited[ny][nx] = True
        return ny,nx,nd


N = int(input())
links = [list(map(int,input().split())) for _ in range(N)]
y = x = N // 2
d = 3
answer = 0
direct = [(0,-1),(1,0),(0,1),(-1,0)]
visited = [[False]*N for _ in range(N)]
visited[y][x] = True
dy = [
    [-1,1,-2,2,-1,1,-1,1,0,0], # 10 # 1%,2%,7%,10%,5%,나머지
    [-1,-1,0,0,0,0,1,1,2,1],
    [-1,1,-2,2,-1,1,-1,1,0,0],
    [1,1,0,0,0,0,-1,-1,-2,-1],
]
dx = [
    [1,1,0,0,0,0,-1,-1,-2,-1],
    [-1,1,-2,2,-1,1,-1,1,0,0],
    [-1,-1,0,0,0,0,1,1,2,1],
    [-1,1,-2,2,-1,1,-1,1,0,0],
]
while True:
    y,x,d = tornado(y,x,d)
    answer = move(y,x,d,answer)
    if (y,x) == (0,0):
        break
print(answer)