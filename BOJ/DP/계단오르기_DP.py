N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [[0]*2 for _ in range(N)]
dp[0][0] = arr[0]
if N > 1:
    dp[1][0] = arr[1]
    dp[1][1] = dp[0][0] + arr[1]
    for i in range(2,N):
        dp[i][0] = max(dp[i-2]) + arr[i]
        dp[i][1] = dp[i-1][0] + arr[i]
    answer = max(dp[N-1])
    print(answer)
else:
    print(dp[0][0])
