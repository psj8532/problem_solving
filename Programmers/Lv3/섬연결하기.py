# 10:40 ~ 11:25
# 최소 신장 트리
def solution(n, costs):
    adj = {i:[] for i in range(n)}
    for s,e,c in costs:
        adj[s].append([e,c])
        adj[e].append([s,c])

    INF = float('inf')
    p = [INF] * n
    mst = [0] * n
    p[0], cnt, answer = 0, 0, 0
    while cnt < n:
        min_v = INF
        posi = -1
        for i in range(n):
            if not mst[i] and p[i] < min_v:
                min_v = p[i]
                posi = i
        mst[posi] = 1
        answer += min_v
        for next, cost in adj[posi]:
            if not mst[next] and cost < p[next]:
                p[next] = cost
        cnt += 1

    return answer

# n	costs	return
ex1 = (4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])	# 4
print(solution(*ex1))