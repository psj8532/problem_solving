MAX, MIN = 1, 0
N = 100
INF = float('inf')

T = int(input())
matches = [int(input()) for _ in range(T)]

count_matches = [2, 3, 4, 5, 6, 7]

numbers = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

dp = [[0] * 2for _ in range(N + 1)]
for i in range(2, 8):
    if i <= 3:
        dp[i][MAX] = numbers[i][0]
    else:
        dp[i][MAX] = int(str(dp[i-2][MAX]) + str(dp[2][MAX]))
    dp[i][MIN] = numbers[i][0]

for i in range(8, N + 1):
    dp[i][MAX] = int(str(dp[i-2][MAX]) + str(dp[2][MAX]))
    min_val = INF
    half = i // 2
    for j in range(2, half + 1):
        vals = []
        val = str(dp[j][MIN]) + str(dp[i - j][MIN])
        if val[0] == '0': vals.append(int('6' + val[1:]))
        else: vals.append(int(val))
        val = str(dp[i - j][MIN]) + str(dp[j][MIN])
        if val[0] == '0': vals.append(int('6' + val[1:]))
        else: vals.append(int(val))

        val = min(vals)

        if val < min_val: min_val = val
    dp[i][MIN] = min_val

for match in matches:
    if match == 6:
        temp = [numbers[match][1], dp[match][MAX]]
        print(*temp)
    else:
        print(*dp[match])