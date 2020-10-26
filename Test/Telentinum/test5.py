def minX(arr):
    # Write your code here
    dp = [0] * len(arr)
    dp[len(arr)-1] = (-1) * arr[len(arr)-1]
    mv = dp[arr[len(arr)-1]]
    if len(arr) == 1:
        return dp[0]
    for i in range(len(arr)-2,-1,-1):
        dp[i] = dp[i+1]-arr[i]
        if dp[i] < mv:
            mv = dp[i]
    if mv < 1:
        answer = 1 - mv + dp[0]
    elif mv > 1:
        answer = mv - 1 - dp[0]
    else:
        answer = mv
    return answer

print(minX([10, -5, 4, -2, 3, 1, -1, -6, -1, 0, -5]))