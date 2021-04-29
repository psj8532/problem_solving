MAX_NUMBER = 20
N = int(input())
numbers = list(map(int,input().split()))
dp = [[0] * N for _ in range(MAX_NUMBER + 1)]
dp[numbers[0]][0] = 1
for col in range(1, N - 1):
    for row in range(MAX_NUMBER + 1):
        if dp[row][col-1]:
            plus = row + numbers[col]
            minus = row - numbers[col]
            if plus <= 20: dp[plus][col] += dp[row][col-1]
            if minus >= 0: dp[minus][col] += dp[row][col-1]

print(dp[numbers[-1]][N-2])