# 15:29 ~ 15:55
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dy = [0,1]
    dx = [1,0]
    for x, y in puddles:
        dp[y-1][x-1] = -1
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            if dp[y][x] == -1: continue
            for dir in range(2):
                ny, nx = y + dy[dir], x + dx[dir]
                if (ny == n or nx == m) or dp[ny][nx] == -1: continue
                dp[ny][nx] = (dp[ny][nx] + dp[y][x]) % 1000000007
    return dp[n-1][m-1]

# m	n	puddles	return
ex1 = (4, 3, [[2, 2]])	# 4
print(solution(*ex1))