def copy(s,t):
    for i in range(N):
        for j in range(N):
            t[i][j] = s[i][j]

def check():
    global max
    for i in range(N):
        for j in range(N):
            if temp[i][j] > max:
                max = temp[i][j]

def move(dir):
    for x in range(N):
        for y in range(N):
            if temp[y][x]:
                ty,tx = y,x
                ny,nx = ty+direct[dir][0],tx+direct[dir][1]
                while 0<=ny<N and 0<=nx<N:
                    if not temp[ny][nx]:
                        temp[ny][nx] = temp[ty][tx]
                        if visited[ty][tx]:
                            visited[ty][tx] = 0
                            visited[ny][nx] = 1
                    elif temp[ny][nx] == temp[ty][tx]:
                        if not visited[ny][nx] and not visited[ty][tx]:
                            temp[ny][nx] *= 2
                            temp[ty][tx] = 0
                            visited[ny][nx] = 1
                        else: break
                    else: break
                    ty,tx = ny,nx
                    ny,nx = ty+direct[dir][0], tx+direct[dir][1]


def perm(k): #방향은 0~3까지 밖에 없는데 순열엔 4도 포함시켜서 인덱스 범위 초과
    if k==5:
        t = a[:]
        s.append(t)
        return
    else:
        in_perm = [False]*5
        for i in range(k):
            in_perm[a[i]] = True
        c = [0]*5
        cnt = 0
        for i in range(5):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[k] = c[i]
            perm(k+1)


direct = [(-1,0),(0,1),(1,0),(0,-1)]
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
temp = [[0]*N for _ in range(N)]
a = [0]*5
s = []
max = 0
perm(0)
for i in range(len(s)):
    for j in range(5):
        visited = [[0] * N for _ in range(N)]
        copy(matrix, temp)
        move(s[i][j])
        check()
print(max)