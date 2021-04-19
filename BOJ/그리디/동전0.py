def dfs(depth, remainder, cnt):
    if depth < 0:
        return cnt
    else:
        coin = coins[depth]
        best_fit = remainder // coin
        ans = dfs(depth - 1, remainder - best_fit * coin, cnt + best_fit)
        if ans: return ans

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
answer = dfs(len(coins) - 1, K, 0)
print(answer)