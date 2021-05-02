Y, X = 0, 1
MOD = 100000
W, H = map(int,input().split())
destination = [0, W - 1]
start = [H - 1, 0]
dp = [[[[0] * 2 for z in range(2)] for x in range(W)] for y in range(H)]

for y in range(H-1, -1, -1):
    dp[y][0][0][0] = 1
for x in range(W):
    dp[H-1][x][1][0] = 1

for y in range(start[Y] - 1, -1, -1):
    for x in range(1, W):
        dp[y][x][0][0] = (dp[y + 1][x][0][0] + dp[y + 1][x][0][1]) % MOD
        dp[y][x][1][0] = (dp[y][x - 1][1][0] + dp[y][x - 1][1][1]) % MOD
        dp[y][x][0][1] = dp[y + 1][x][1][0] % MOD
        dp[y][x][1][1] = dp[y][x - 1][0][0] % MOD

answer = 0
for direction in range(2):
    for turn in range(2):
        answer = (answer + dp[destination[Y]][destination[X]][direction][turn]) % MOD
print(answer)