N, K = map(int,input().split())
coins = []
DP = [0] * (K+1)
for _ in range(N):
    coins.append(int(input()))
DP[0] = 1
for i in range(1, K+1):
    DP[i] = 0 if i % coins[0] else 1
for i in range(1,N):
    for j in range(K+1):
        if j < coins[i]: continue
        DP[j] += DP[j-coins[i]]
print(DP[K])