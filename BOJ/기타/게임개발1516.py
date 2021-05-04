def dfs(building, cost):
    global answer

    if not precedings[building]:
        answer = max(answer, cost)
    else:
        for preceding in precedings[building]:
            dfs(preceding, cost + times[preceding])
    return

N = int(input())
times = {}
precedings = {}
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    times[i], precedings[i] = info[0], info[1:-1]

for i in range(1, N + 1):
    answer = 0
    dfs(i, times[i])
    print(answer)
