from collections import deque

def start_bfs(sy,sx,d):
    deq = deque()
    if (sy,sx) in start and (sy,sx) == start[(sy,sx)]:
        Cs.append([sy,sx,d])
        return
    deq.append([sy,sx,d])
    visited[sy][sx] = True

    while deq:
        y,x,d = deq.popleft()
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and not matrix[ny][nx] and start.get((ny,nx)) is not None: # 도착 지점 정보 못찾겠음
                Cs.append([ny , nx, d + 1])
                deq.append([ny, nx, d + 1])
                visited[ny][nx] = True
            elif 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and not matrix[ny][nx]:
                deq.append([ny, nx, d + 1])
                visited[ny][nx] = True


# def dest_bfs(lst):
#     y,x,fuel,idx = lst
#     print('목적지로 출발 전',y,x)
#     print('연료',fuel)
#     if end[y][x] == idx and fuel <= tank:
#         dest.append(y)
#         dest.append(x)
#         return 0
#     deq=deque()
#     deq.append([y,x,0])
#     visited[y][x] = True
#
#     while deq:
#         y,x,d = deq.popleft()
#         for dir in range(4):
#             ny, nx = y + direct[dir][0], x + direct[dir][1]
#             if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and end[ny][nx] == idx and fuel+d+1 <= tank:
#                 dest.append(ny)
#                 dest.append(nx)
#                 print('도착',ny,nx,d+1)
#                 return d+1
#             elif 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and end[ny][nx] != 1 and fuel+d+1 <= tank:
#                 deq.append([ny, nx, d + 1])
#                 visited[ny][nx] = True
#     return -1

def dest_bfs(lst):
    sy,sx,fuel,idx = lst
    print('목적지로 출발 전',sy,sx)
    print('연료',fuel)
    if (sy,sx) in start and (sy,sx) == start[(sy,sx)] and fuel <= tank:
        dest.append(sy)
        dest.append(sx)
        return 0
    deq=deque()
    deq.append([sy,sx,0])
    visited[sy][sx] = True

    while deq:
        y,x,d = deq.popleft()
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and not matrix[ny][nx] and (sy,sx) in start and (ny,nx) == start[(sy,sx)] and fuel+d+1 <= tank:
                dest.append(ny)
                dest.append(nx)
                print('도착',ny,nx,d+1)
                return d+1
            elif 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and not matrix[ny][nx] and fuel+d+1 <= tank:
                deq.append([ny, nx, d + 1])
                visited[ny][nx] = True
    return -1

direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M,tank = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
# end = [[0]*N for _ in range(N)]

sy,sx = map(int,input().split())
sy,sx = sy-1,sx-1
customer = {}
start = {}
for i in range(2,M+2):
    t = list(map(int,input().split()))
    ts,te = t[:2],t[2:]
    ts[0], ts[1] = ts[0] - 1, ts[1] - 1
    te[0], te[1] = te[0] - 1, te[1] - 1
    start[(ts[0],ts[1])] = (te[0],te[1])
    customer[(ts[0],ts[1])] = False

isEnd = False
while not isEnd:
    isEnd = True
    Cs = []
    visited = [[False] * N for _ in range(N)]
    print('전체연료', tank)
    print('출발 위치',sy,sx)
    start_bfs(sy,sx,0)

    # 가까운 후보 추려내기
    if not Cs:
        fl = -1
        break
    c = min(Cs, key=lambda x: (x[2],x[0],x[1]))
    print('탑승 위치', c)

    # 목적지 찾기
    dest = []
    visited = [[False]*N for _ in range(N)]
    fl = dest_bfs(c)
    print('이동거리', fl)
    print('목적지', dest)
    if fl == -1:
        isEnd = True
        break
    else:
        sy,sx = dest
        tank = tank - c[2] - fl + fl * 2
        print('남은 연료', tank)
        print('-----')
        customer[(c[0],c[1])] = True

    for k,v in customer.items():
        if not customer[k]:
            isEnd = False

if fl == -1:
    print(-1)
else:
    print(tank)

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