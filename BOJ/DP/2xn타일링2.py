# 11:37 ~
# n이 3일때, 잘못 구해서 참고
N = int(input())
DP = [0]*(N+1)
DP[0], DP[1] = 1, 1
if N == 1: print(DP[1])
else:
    for i in range(2,N+1):
        DP[i] = (2 * DP[i-2] + DP[i-1]) % 10007
    print(DP[N])