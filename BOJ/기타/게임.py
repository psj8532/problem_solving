def move(y, x, cnt, d):
    return y + direct[d][Y] * cnt, x + direct[d][X] * cnt

def dfs(y, x ,moving_count):
    if visited[y][x]: return -1
    visited[y][x] = True
    dp[y][x] = moving_count

    for dir in range(4):
        ny, nx = move(y, x, int(board[y][x]), dir)
        if 0 <= ny < N and 0 <= nx < M and dp[y][x] + 1 > dp[ny][nx] and board[ny][nx] != 'H':
            ans = dfs(ny, nx, dp[y][x] + 1)
            if ans == -1: return -1
    visited[y][x] = False
    return 0

Y, X = 0, 1
N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
direct = [(-1,0), (0,1), (1,0), (0,-1)]

dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = dfs(0, 0, 1)
if answer != -1:
    answer= 0
    for i in range(N):
        for j in range(M):
             if dp[i][j] > answer:
                 answer = dp[i][j]
print(answer)