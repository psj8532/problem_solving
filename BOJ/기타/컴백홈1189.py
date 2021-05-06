def dfs(y, x, distance):
    global answer
    if (y, x) == (0, C - 1):
        if distance == K:
            answer += 1
    else:
        for dir in range(DIRECTION):
            ny, nx = y + direction[dir][Y], x + direction[dir][X]
            if 0 <= ny < R and 0 <= nx < C and not visit[ny][nx] and matrix[ny][nx] != 'T' and distance + 1 <= K:
                visit[ny][nx] = True
                dfs(ny, nx, distance + 1)
                visit[ny][nx] = False

DIRECTION = 4
Y, X = 0, 1
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
R, C, K = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
visit[R - 1][0] = True
answer=  0
dfs(R - 1, 0, 1)
print(answer)