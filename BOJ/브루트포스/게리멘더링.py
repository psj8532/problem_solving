from itertools import combinations
from collections import deque

def check_ward(here, cities):
    visited = [False] * N
    visited[here] = True
    deq = deque([here])
    people = cities_people[here]
    while deq:
        h = deq.popleft()
        for next in range(N):
            if not visited[next] and adj[h][next] and next in cities:
                visited[next] = True
                deq.append(next)
                people += cities_people[next]
    for city in cities:
        if not visited[city]: return 0
    return people


N = int(input())
cities_people = list(map(int,input().split()))
adj = [[0] * N for _ in range(N)]
for start in range(N):
    info = list(map(int,input().split()))
    for end in info[1:]:
        end -= 1
        adj[start][end] = 1
        adj[end][start] = 1

half = N // 2
answer = 9876543210
for perm_size in range(1,half + 1):
    perm = list(map(list,combinations(range(N), perm_size)))
    for cities1 in perm:
        cities2 = []
        for city in range(N):
            if city in cities1: continue
            cities2.append(city)
        peoples1 = check_ward(cities1[0], cities1)
        peoples2 = check_ward(cities2[0], cities2)
        if peoples1 and peoples2:
            diff = abs(peoples1 - peoples2)
            answer = min(diff, answer)

if answer == 9876543210: print(-1)
else: print(answer)
