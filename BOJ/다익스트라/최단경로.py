import sys
sys.stdin = open("최단경로.txt", "r")

V,E = map(int,input().split())
start = int(input())
adj = {i:[] for i in range(V+1)}
for i in range(E):
    u,v,w = map(int,input().split())
    adj[u].append([v,w])
INF = float('inf')
s = [0]*(V+1)
dist = [INF]*(V+1)
cnt = 0
dist[start] = 0
while cnt<V:
    min = INF
    for i in range(1, V+1):
        if not s[i] and dist[i] < min:
            min = dist[i]
            node = i
    cnt += 1
    s[node] = 1
    for w,cost in adj[node]:
        c = dist[node]+cost
        if c < dist[w]:
            dist[w] = c
for i in range(1, len(dist)):
    if dist[i]<INF:
        print(dist[i])
    else:
        print('INF')