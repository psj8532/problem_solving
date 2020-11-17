N = int(input())
dp = [1] * 10
dp[0] = 0
for i in range(1,N):
    temp = [0] * 10
    for j in range(10):
        nj = j - 1
        if 0 <= nj:
            temp[j] += dp[nj]
        nj = j + 1
        if nj < 10:
            temp[j] += dp[nj]
    dp = temp[:]
print(sum(dp)%1000000000)