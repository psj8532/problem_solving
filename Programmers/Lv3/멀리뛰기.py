# 13:34 ~ 13:50
def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n-1):
        dp[i+1] = (dp[i] + dp[i+1]) % 1234567
        dp[i+2] = (dp[i] + dp[i+2]) % 1234567
    dp[n] = (dp[n] + dp[n-1]) % 1234567
    return dp[n]

print(solution(4))