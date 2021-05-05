from sys import stdin

N, M = map(int, stdin.readline().split())
numbers = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][0] = numbers[i][0]
    for j in range(1, N):
        dp[i][j] = dp[i][j - 1] + numbers[i][j]
for _ in range(M):
    sy, sx, ey, ex = map(int, stdin.readline().split())
    sy, sx, ey, ex = sy - 1, sx - 1, ey - 1, ex - 1
    answer = 0
    for i in range(sy, ey + 1):
        if sx: answer += (dp[i][ex] - dp[i][sx - 1])
        else: answer += dp[i][ex]
    print(answer)