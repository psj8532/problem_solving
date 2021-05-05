import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[0] = numbers[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + numbers[i]
for _ in range(M):
    answer = 0
    start, end = map(int, sys.stdin.readline().split())
    start, end = start - 1, end - 1
    if start: answer = dp[end] - dp[start - 1]
    else: answer = dp[end]
    print(answer)