def get_some(a,b):
    if a <= b:
        return a
    else:
        return b


def solution(N):
    dp = [house[0][0],house[0][1],house[0][2]]
    for i in range(1,N):
        temp = [0,0,0]
        temp[0], temp[1], temp[2] = dp[0], dp[1], dp[2]
        temp[0] = house[i][0] + get_some(dp[1], dp[2])
        temp[1] = house[i][1] + get_some(dp[0], dp[2])
        temp[2] = house[i][2] + get_some(dp[0], dp[1])
        dp[0], dp[1], dp[2] = temp[0], temp[1], temp[2]
    return min(dp)


N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
print(solution(N))