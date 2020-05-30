from _collections import deque

def find_enemy():
    for y in range(N - 1, -1, -1):
        for x in range(M):
            if matrix[y][x]:
                return True
    return False

def select_kill(s):
    min_y, min_x = s[0][0], s[0][1]
    for idx in range(1, len(s)):
        if s[idx][1] < min_x:
            min_y, min_x = s[idx][0], s[idx][1]
    if (min_y, min_x) not in kill_list:
        kill_list.append((min_y, min_x))

def copy():
    for y in range(N):
        for x in range(M):
            matrix[y][x] = matrix_temp[y][x]

def change():
    for idx in range(len(kill_list)):
        r, c = kill_list[idx][0], kill_list[idx][1]
        matrix[r][c] = 0

def move():
    for y in range(N - 2, -1, -1):
        for x in range(M):
            if matrix[y][x]:
                matrix[y + 1][x] = 1
                matrix[y][x] = 0
            else:
                matrix[y + 1][x] = 0

def bfs(y,x,d):
    deq = deque()
    visited = [[0]*M for _ in range(N)]
    s = []
    deq.append((y,x,d))
    if matrix[y][x]: #중첩 if문을 and로 한번에 처리할땐 예외 상황까지 신중하게 고려해보고 쓸 것
        if (y,x) not in kill_list:
            kill_list.append((y,x))
        return
    visited[y][x] = 1
    flag = False
    while deq:
        here = deq.popleft()
        y,x,d = here[0],here[1],here[2]
        if flag and d!=rd:
            #최대 좌표값 찾기
            select_kill(s)
            return

        for dir in range(len(direct)):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<N and 0<=new_x<M and matrix[new_y][new_x] and not visited[new_y][new_x] and d+1<=D:
                s.append((new_y,new_x))
                rd = d
                flag = True
            elif not s and 0<=new_y<N and 0<=new_x<M and not visited[new_y][new_x] and d+1<D:
                deq.append((new_y,new_x,d+1))
                visited[new_y][new_x] = 1
        if s and not deq:
            select_kill(s)


direct = [(-1,0),(0,1),(0,-1)]
N,M,D = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
matrix_temp = [[0]*M for _ in range(N)]
max_kill = 0
for i in range(N):
    for j in range(M):
        matrix_temp[i][j] = matrix[i][j]
for i in range(M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            copy()
            isExist = True
            kill = 0
            while isExist:
                isExist = False
                if find_enemy():
                    isExist = True
                if not isExist: break
                kill_list = []
                bfs(N-1,i,1)
                bfs(N-1,j,1)
                bfs(N-1,k,1)
                kill += len(kill_list)
                if kill_list:
                    change() #죽인 적의 좌표 변경
                move() #적이동
            #죽인 적이 최대인지 비교
            if kill > max_kill:
                max_kill = kill
print(max_kill)