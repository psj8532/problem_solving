from _collections import deque


def dfs():
    global min
    stack = [E]
    while stack:
        cur = stack.pop()
        for pre,co in dist_list[cur]:
            stack.append(pre)
            if dist[E] - co < min:
                min = dist[E] - co


N,S,E =  map(int,input().split())
adj = {i:[] for i in range(1,N+1)}
if S == E:
    print(0)
else:
    for i in range(N-1):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
        adj[e].append([s,c])
    INF = float('inf')
    dist = [INF] * (N+1)
    dist_list = {i:[] for i in range(1,N+1)}
    deq = deque()
    deq.append(S)
    dist[S] = 0
    while deq:
        here = deq.popleft()
        for next,cost in adj[here]:
            if dist[here] + cost < dist[next]:
                dist[next] = dist[here] + cost
                deq.append(next)
                dist_list[next] = []
                dist_list[next].append([here,cost])
            elif dist[here] + cost == dist[next]:
                deq.append(next)
                dist_list[next].append([here,cost])
    min = INF
    dfs()
    print(min)