import sys
sys.stdin = open("최소비용구하기.txt", "r")

N = int(input())
M = int(input())
adj = {i:[] for i in range(N+1)}
for i in range(M):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
start, end = map(int,input().split())
INF = float('inf')
price = [INF]*(N+1)
selected = [0]*(N+1)
cnt = 0
price[start] = 0
while cnt<N:
    min = INF
    for i in range(1, N+1):
        if not selected[i] and price[i]<min:
            min = price[i]
            node = i
    selected[node] = 1
    cnt += 1
    for w,cost in adj[node]:
        c = price[node]+cost
        if c < price[w]:
            price[w] = c
print(price[end])