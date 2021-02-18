# 19:50 ~ 20:48
def out(r, c, n):
    global answer
    if 0 <= r < B and 0 <= c < A: return False
    else:
        answer = 'Robot ' + str(n) + ' crashes into the wall'
        return True

def crash(r, c, n):
    global answer
    if land[r][c]:
        answer = 'Robot ' + str(n) + ' crashes into robot ' + str(land[r][c])
        return True
    else: return False

answer = 'OK'
Y, X, D = 0, 1, 2
A, B = map(int,input().split())
N, M = map(int,input().split())
robot = {i:[] for i in range(1, N+1)}
LEFT = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N',
}
RIGHT = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}
DIRECT = {
    'N': [-1,0],
    'E': [0,1],
    'S': [1,0],
    'W': [0,-1],
}
land = [[0] * A for _ in range(B)]
for num in range(1, N+1):
    x, y, dir = input().split()
    x, y = int(x), int(y)
    y , x = B - y, x - 1
    robot[num] = [y, x, dir]
    land[y][x] = num
for _ in range(M):
    num, command, move = input().split()
    num, move = int(num), int(move)
    cnt = 1
    y, x = robot[num][Y], robot[num][X]
    while cnt <= move:
        if command == 'L':
            robot[num][D] = LEFT[robot[num][D]]
        elif command == 'R':
            robot[num][D] = RIGHT[robot[num][D]]
        else:
            ny, nx = y + DIRECT[robot[num][D]][Y], x + DIRECT[robot[num][D]][X]
            if out(ny, nx, num): break
            if crash(ny, nx, num): break
            robot[num][Y], robot[num][X] = ny, nx
            land[y][x], land[ny][nx] = 0, num
            y, x = ny, nx
        cnt += 1
    if answer != 'OK': break
print(answer)