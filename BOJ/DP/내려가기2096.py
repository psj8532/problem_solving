COL = 3
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
max_dp, min_dp = matrix[0][:], matrix[0][:]
for i in range(1, N):
    new_max_dp, new_min_dp = [0] * COL, [float('inf')] * COL
    for j in range(COL):
        new_max_dp[j] = max(new_max_dp[j], max_dp[j] + matrix[i][j])
        new_min_dp[j] = min(new_min_dp[j], min_dp[j] + matrix[i][j])
        if 0 <= j - 1:
            new_max_dp[j] = max(new_max_dp[j], max_dp[j - 1] + matrix[i][j])
            new_min_dp[j] = min(new_min_dp[j], min_dp[j - 1] + matrix[i][j])
        if j + 1 < COL:
            new_max_dp[j] = max(new_max_dp[j], max_dp[j + 1] + matrix[i][j])
            new_min_dp[j] = min(new_min_dp[j], min_dp[j + 1] + matrix[i][j])
    max_dp, min_dp = new_max_dp[:], new_min_dp[:]

print(max(max_dp), min(min_dp))