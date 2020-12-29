def white(r,c,nr,nc,dir,n):
    idx = chess[(r,c)].index(n)
    for number in chess[(r,c)][idx:]:
        chess[(nr,nc)].append(number)
        horse[number][0], horse[number][1] = nr, nc
    for i in range(len(chess[(r,c)])-1, idx-1, -1):
        chess[(r,c)].pop()

def red(r,c,nr,nc,dir,n):
    idx = chess[(r, c)].index(n)
    for number in range(len(chess[(r, c)])-1,idx-1,-1):
        tnum = chess[(r, c)][number]
        horse[tnum][0], horse[tnum][1] = nr, nc
    for i in range(len(chess[(r,c)])-1, idx-1, -1):
        chess[(r,c)].pop()

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
N, K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
chess = {}
for i in range(N):
    for j in range(N):
        chess[(i,j)] = []
horse = {}
for i in range(1,K+1):
    horse[i] = list(map(int,input().split()))
    for j in range(3):
        horse[i][j] -= 1
    chess[(horse[i][0],horse[i][1])].append(i)
time = 0
flag = False
while time < 1000 and not flag:
    for num in range(1,K+1):
        y, x, d = horse[num][0], horse[num][1], horse[num][2]
        ny, nx = y + dy[d], x + dx[d]
        # 이동하려는 곳의 색깔 확인
        if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 0:
            white(y,x,ny,nx,d,num)
            if len(chess[(ny,nx)]) >= 4:
                flag = True
                break
        elif 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 1:
            red(y,x,ny,nx,d,num)
            if len(chess[(ny,nx)]) >= 4:
                flag = True
                break
        else:
            if d == 0 or d == 2:
                d += 1
            else:
                d -= 1
            ny, nx = y + dy[d], x + dx[d]
            # 흰,빨,파 확인
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 0:
                white(y, x, ny, nx, d, num)
                if len(chess[(ny, nx)]) >= 4:
                    flag = True
                    break
            elif 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 1:
                red(y, x, ny, nx, d, num)
                if len(chess[(ny, nx)]) >= 4:
                    flag = True
                    break
            horse[num][2] = d
    time += 1

if time >= 1000:
    print(-1)
else:
    print(time)