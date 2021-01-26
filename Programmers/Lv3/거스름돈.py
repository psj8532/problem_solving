# 
def solution(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for j in range(coin, n+1):
            dp[j] += dp[j-coin]
    return dp[n] % 1000000007


# n	money	result
ex1 = (5, [1,2,5])	# 4
ex2 = (100000, [i for i in range(1,101)])
ex3 = (7, [2,4,5])
ex4 = (9, [3])
print(solution(*ex4))