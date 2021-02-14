n, K = map(int,input().split())
money = []
for _ in range(n):
    money.append(int(input()))
money = list(set(money))
money.sort()
N, INF = len(money), float('inf')
DP = [INF] * (K+1)
DP[0] = 0

for coin in money:
    for j in range(coin, K+1):
        DP[j] = min(DP[j], DP[j - coin] + 1)
if DP[K] == INF: print(-1)
else: print(DP[K])

# 반례 (greedy가 안되는 이유)
# 3 34
# 1
# 17
# 30