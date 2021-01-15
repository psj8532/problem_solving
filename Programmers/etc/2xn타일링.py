# 19:03 ~ 20:09
def solution(n):
    dp = [0] * 600001
    dp[1], dp[2] = 1, 2
    if n > 2:
        for i in range(3,n+1):
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    return dp[n]

ex1 = 4 # 5
ex2= 7
ex3 = 60000
ex4 = 7
print(solution(ex4))