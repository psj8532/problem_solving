def change(y,x):
    ny = y
    while 0<=ny<11 and matrix[ny+1][x] == '.':
        matrix[ny][x],matrix[ny+1][x] = matrix[ny+1][x],matrix[ny][x]
        ny += 1


def check():
    for c in range(6):
        flag = False
        for r in range(11,-1,-1):
            if matrix[r][c] != '.' and flag:
                change(r,c)
            elif matrix[r][c] == '.':
                flag = True


def bfs(y,x,c):
    global isEnd
    queue = []
    front = 0
    visited = [[0] * 6 for _ in range(12)]
    queue.append((y,x))
    visited[y][x] = 1
    while front != len(queue):
        here = queue[front]
        y,x = here[0],here[1]
        for dir in range(4):
            ny,nx = y+direct[dir][0],x+direct[dir][1]
            if 0<=ny<12 and 0<=nx<6 and matrix[ny][nx] == c and not visited[ny][nx]:
                queue.append((ny,nx))
                visited[ny][nx] = 1
        front += 1
    if front>=4:
        for idx in range(front):
            ny,nx = queue[idx][0],queue[idx][1]
            matrix[ny][nx] = '.'
        isEnd = False


matrix = [list(input()) for _ in range(12)]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
isEnd = False
while not isEnd:
    isEnd = True
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                bfs(i,j,matrix[i][j])
    if not isEnd:
        cnt += 1
        check()
print(cnt)