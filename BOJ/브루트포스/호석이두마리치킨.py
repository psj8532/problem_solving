from itertools import combinations
from _collections import deque

def bfs(here, depth, chicken_house):
    if here in chicken_house: return 0
    deq = deque([[here, depth]])
    visited = [False] * (N + 1)
    visited[here] = True

    while deq:
        h, d = deq.popleft()
        if h in chicken_house:
            return 2 * d
        for next in adj[h]:
            if not visited[next]:
                visited[next] = True
                deq.append([next, d + 1])


CHICKEN_CNT = 2
answer = [0,0,9876543210]
N, M = map(int,input().split())
adj = {i:[] for i in range(N+1)}
for _ in range(M):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

perm = list(map(list, combinations(range(1, N + 1), CHICKEN_CNT)))
for chicken_list in perm:
    chicken_house = sorted(chicken_list)
    distance = 0
    for house in range(1, N + 1):
        distance += bfs(house, 0 , chicken_house)
    if distance == answer[2] and chicken_house[0] <= answer[0]:
        if (chicken_house[0] == answer[0] and chicken_house[1] < answer[1]) or (chicken_house[0] < answer[0]):
            answer[0], answer[1] = chicken_house[0], chicken_house[1]
    elif distance < answer[2]:
        answer[0], answer[1], answer[2] = chicken_house[0], chicken_house[1], distance
print(*answer)