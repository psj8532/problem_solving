from itertools import combinations

def dfs(here, cnt, cand):
    stack = [here]
    while stack:
        here = stack.pop()
        if visited[here]: continue
        visited[here] = 1
        cnt += people[here]
        for next in adj[here]:
            if not visited[next] and next in cand:
                stack.append(next)
    return cnt

N = int(input())
people = [0] + list(map(int,input().split()))
adj, answer = {}, 10000
for i in range(1, N+1):
    info = list(map(int,input().split()))
    adj[i] = []
    for j in range(1, info[0]+1):
        adj[i].append(info[j])

for i in range(1,N // 2 + 1):
    comb = list(combinations(range(1,N+1), i))
    for left in comb:
        left = list(left)
        right = []
        for j in range(1,N+1):
            if j in left: continue
            right.append(j)
        visited = [0] * (N+1)
        l_cnt = dfs(left[0], 0, left)
        r_cnt = dfs(right[0], 0, right)
        for i in range(1, N+1):
            if not visited[i]: break
        else:
            diff = abs(l_cnt - r_cnt)
            answer = min(diff, answer)

if answer == 10000: print(-1)
else: print(answer)