from _collections import deque


def partition(L):
    t_matrix = [[0] * (2 ** N) for _ in range(size)]
    Lsize = 2**L
    # 분할
    for i in range(0,size,Lsize):
        for j in range(0,size,Lsize):
            # 시계 방향으로 회전
            si,ei,sj,ej = i,i+Lsize,j,j+Lsize
            for r in range(si,ei):
                ny = r % (Lsize)
                for c in range(sj,ej):
                    nx = c % (Lsize)
                    t_matrix[si+nx][ej-1-ny] = matrix[r][c]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = t_matrix[i][j]


def check(y,x,cnt):
    deq = deque()
    deq.append((y, x))
    visited[y][x] = True

    while deq:
        y, x = deq.popleft()
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < size and 0 <= nx < size and not visited[ny][nx] and matrix[ny][nx] > 0:
                deq.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    return cnt


N,Q = map(int,input().split())
size = 2**N
matrix = [list(map(int,input().split())) for _ in range(size)]
steps = list(map(int,input().split()))
direct = [(-1,0),(0,1),(1,0),(0,-1)]

for idx,step in enumerate(steps):
    # 분할
    if step > 0:
        partition(step)
    # 얼음 녹이기
    deq = deque()
    for i in range(size):
        for j in range(size):
            cnt = 0
            for dir in range(4):
                ny, nx = i + direct[dir][0], j + direct[dir][1]
                if 0 <= ny < size and 0 <= nx < size and matrix[ny][nx] > 0:
                    cnt += 1
            if matrix[i][j] > 0 and cnt < 3: # 원본에 바로 녹이면 안됨 # 한 턴에 녹일 땐, 모두 동시에 녹이는 것이므로 # deq은 녹일 얼음의 후보 이므로 자기 자신도 얼음이 있어야함
                deq.append((i,j))
    while deq:
        y,x = deq.popleft()
        matrix[y][x] -= 1
# 남은 얼음의 양 , 덩어리 최대 크기 확인
max_cnt = 0
total = 0
visited = [[False] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        total += matrix[i][j]
        if not visited[i][j] and matrix[i][j] > 0:
            result = check(i,j,1)
            if result > max_cnt:
                max_cnt = result

print(total)
print(max_cnt)