# 20:04 ~ 20:25
def solution(triangle):
    N = len(triangle)
    M = len(triangle[N-1])
    dp = [0] * M
    dp[0] = triangle[0][0]
    for i in range(N-1):
        temp = [0] * M
        for j in range(len(triangle[i])):
            temp[j] = max(triangle[i+1][j]+dp[j],temp[j])
            temp[j+1] = max(triangle[i+1][j+1]+dp[j],temp[j+1])
        dp = temp[:]

    return max(dp)

ex1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]   # 30
print(solution(ex1))