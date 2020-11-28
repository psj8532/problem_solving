from _collections import deque

def find_customer(y,x,d):
    if customers.get((y,x)) is not None and c_visited[y][x]:
        Cs.append([y,x,d])
        return
    deq = deque()
    deq.append([y,x,d])
    visited[y][x] = True

    while deq:
        y,x,d = deq.popleft()
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < N and 0 <= nx < N and not matrix[ny][nx] and not visited[ny][nx] and c_visited[ny][nx]:
                Cs.append([ny,nx,d+1])
                deq.append([ny,nx,d+1])
                visited[ny][nx] = True
            elif 0 <= ny < N and 0 <= nx < N and not matrix[ny][nx] and not visited[ny][nx]:
                deq.append([ny, nx, d + 1])
                visited[ny][nx] = True


def move(lst):
    y,x,fuel = lst
    ey,ex = customers[(y,x)]
    if (y,x) == (ey,ex):
        dest.append(y)
        dest.append(x)
        return 0
    deq = deque()
    deq.append([y,x,0])
    visited[y][x] = True

    while deq:
        y,x,d = deq.popleft()
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < N and 0 <= nx < N and not matrix[ny][nx] and not visited[ny][nx] and (ny,nx) == (ey,ex) and fuel+d+1 <= tank:
                dest.append(ny)
                dest.append(nx)
                return d+1
            elif 0 <= ny < N and 0 <= nx < N and not matrix[ny][nx] and not visited[ny][nx] and fuel+d+1 <= tank:
                deq.append([ny,nx,d+1])
                visited[ny][nx] = True

    return -1

def check():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if c_visited[i][j]:
                cnt += 1
    if cnt > 0: # 아직 남아있는 손님이 있다면
        return False
    else:
        return True


answer = -1
direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M,tank = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
sy,sx = map(int,input().split())
sy,sx = sy-1,sx-1
c_visited = [[False]*N for _ in range(N)] # 손님이 있으면 True
customers = {}
for i in range(M):
    t = list(map(int,input().split()))
    for j in range(4):
        t[j] -= 1
    ts, te = t[:2], t[2:]
    customers[(ts[0],ts[1])] = (te[0],te[1])
    c_visited[ts[0]][ts[1]] = True

isEnd = False
while not isEnd:
    isEnd = True
    Cs = []
    visited = [[False]*N for _ in range(N)]

    find_customer(sy,sx,0)
    # 손님 후보 뽑기
    if not Cs:
        answer = -1
        break
    c = min(Cs, key=lambda x:(x[2],x[0],x[1]))
    # 손님 태우고 출발
    # print('출발',c[0],c[1],'거리',c[2])
    dest = []
    visited = [[False] * N for _ in range(N)]
    fl = move(c)
    # print('도착',*dest)
    if fl == -1:
        answer = -1
        break
    else:
        tank = tank - c[2] + fl
        # print('남은 연료: ', tank)
        sy,sx = dest
        c_visited[c[0]][c[1]] = False

    if not check():
        isEnd = False
    else:
        answer = tank

print(answer)

# 6 3 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 1 6 4 2
# 5 4 1 6
# 4 2 3 5

# 6 4 15
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 6
# 5 4 1 6
# 4 2 3 5
# 1 6 5 4

# 6 4 100
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 6 5
# 1 6 2 2
# 1 6 3 5
# 1 6 5 4
# 1 6 1 1

# 6 5 19
# 1 0 0 0 1 0
# 1 0 1 0 1 0
# 1 0 1 0 1 0
# 1 0 1 0 1 0
# 1 0 1 0 1 0
# 0 0 1 0 0 0
# 1 3
# 6 1 1 6
# 1 6 6 2
# 5 2 2 4
# 6 5 6 6
# 4 6 1 2