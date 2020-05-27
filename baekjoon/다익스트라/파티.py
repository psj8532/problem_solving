import sys
sys.stdin = open("파티.txt", "r")
from _collections import deque

N,M,X = map(int,input().split())
adj = {i:[] for i in range(1,N+1)}
max = 0
INF = float('inf')
for i in range(M):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
for i in range(1,N+1):
    dist = [INF]*(N+1)
    dist[i] = 0
    deq = deque()
    deq.append(i)
    while deq:
        h = deq.popleft()
        for n,cost in adj[h]:
            if dist[h]+cost < dist[n]:
                if h != X:
                    deq.append(n)
                dist[n] = dist[h]+cost
    deq.append(X)
    temp = dist[X]
    dist = [INF]*(N+1)
    dist[X] = temp
    while deq:
        h = deq.popleft()
        for n, cost in adj[h]:
            if dist[h] + cost < dist[n]:
                if h != i:
                    deq.append(n)
                dist[n] = dist[h] + cost
    if dist[i]>max:
        max = dist[i]
print(max)