import heapq

V, E = map(int,input().split())
adj = {i:[] for i in range(1, V + 1)}
for _ in range(E):
    start, end, cost = map(int,input().split())
    adj[start].append([end, cost])
    adj[end].append([start, cost])

INF = float('inf')
weight = [INF] * (V + 1)
mst = [False] * (V + 1)
weight[1], answer, cnt = 0, 0, 0
cand = [(0, 1)]
heapq.heapify(cand)

while cnt < V:
    c, node = heapq.heappop(cand)
    if mst[node]: continue
    mst[node] = True
    answer += c

    for next, cost in adj[node]:
        if cost < weight[next]:
            weight[next] = cost
            heapq.heappush(cand, (cost, next))

    cnt += 1

print(answer)
