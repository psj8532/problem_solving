# 11:19 ~ 11:33
N = int(input())
DP = [0]*(N+1)
if N == 1: print(1)
elif N == 2: print(2)
else:
    DP[1], DP[2] = 1, 2
    for i in range(3,N+1):
        DP[i] = (DP[i-2] + DP[i-1]) % 10007
    print(DP[N])