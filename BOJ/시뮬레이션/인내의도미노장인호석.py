# 15:44 ~
from _collections import deque

N, M, R = map(int,input().split())
check = [['S']*M for _ in range(N)]
direction = {
    'N': [-1,0],
    'E': [0,1],
    'S': [-1,0],
    'W': [0,-1],
}
Y, X = 0, 1
domino = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for _ in range(R):
    ay, ax, ad = input().split()
    dy, dx = map(int,input().split())
    ay, ax, dy, dx = int(ay) - 1, int(ax) - 1, dy - 1, dx - 1
    cand = deque()
    if check[ay][ax] == 'S':
        cand.append([ay,ax,domino[ay][ax]])
        check[ay][ax] = 'F'
        answer += 1
    while cand:
        y, x, k = cand.popleft()
        move = 1
        while move < k:
            ny, nx = y + move * direction[ad][Y], x + move * direction[ad][X]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] == 'S':
                    cand.append([ny, nx, domino[ny][nx]])
                    answer += 1
                check[ny][nx] = 'F'
            move += 1
    check[dy][dx] = 'S'

print(answer)
for row in check:
    print(*row)