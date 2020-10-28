N = int(input())
triangle = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * 500
dp[0] = triangle[0][0]
for i in range(1,N):
    temp = [0] * 500
    for j in range(len(triangle[i])):
        if j == 0:
            temp[0] = dp[0] + triangle[i][0]
        elif j == len(triangle[i])-1:
            temp[j] = dp[j-1] + triangle[i][j]
        else:
            temp[j] = max(dp[j-1]+triangle[i][j], dp[j]+triangle[i][j])
    dp = temp[:]
print(max(dp))