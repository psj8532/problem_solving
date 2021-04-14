import heapq

N = int(input())
M = int(input())
adj = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    s, e, c = map(int,input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

INF = float('inf')
weight = [INF] * (N + 1)
mst = [False] * (N + 1)
weight[1] = 0
cand = [(weight[1], 1)]
heapq.heapify(cand)
answer, cnt = 0, 0

while cnt < N:
    c, node = heapq.heappop(cand)
    if mst[node]: continue
    mst[node] = True
    answer += c

    for next, cost in adj[node]:
        if cost < weight[next]:
            heapq.heappush(cand, (cost, next))
            weight[next] = cost

    cnt += 1

print(answer)