N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [[0]*3 for _ in range(N)]
dp[0][0] = arr[0]
if N > 1:
    dp[1][0] = arr[1]
    dp[1][1] = dp[0][0] + arr[1]
    for i in range(2,N):
        dp[i][0] = max(dp[i-2]) + arr[i]
        dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + arr[i]
        if i > 2: dp[i][2] = max(dp[i-3]) + arr[i]
    answer1 = max(dp[N-2])
    answer2 = max(dp[N-1])
    print(answer1 if answer1 >= answer2 else answer2)
else:
    print(dp[0][0])
