def dfs(here, distance):
    global answer
    if destination <= here:
        answer = distance
    else:
        for nh in range(here, destination + 1):
            if pointer[nh]:
                for next, cost in shortcut[nh]:
                    new_dist = nh - here + distance + cost
                    if new_dist <= answer:
                        dfs(next, new_dist)
        else:
            new_dist = nh - here + distance
            if new_dist <= answer:
                dfs(nh, new_dist)

N, destination = map(int,input().split())
answer = float('inf')
pointer = [0] * (destination+1)
shortcut = {}
for _ in range(N):
    s, e, d = map(int,input().split())
    if e > destination: continue
    if s in shortcut: shortcut[s].append([e, d])
    else: shortcut[s] = [[e, d]]
    pointer[s] = 1

dfs(0, 0)

print(answer)