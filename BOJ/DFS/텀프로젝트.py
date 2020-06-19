def dfs(s):
    global cnt
    if visited[s]:
        if first != s:
            cnt += 1
        else:
            for x in range(len(visit)):
                visited[visit.pop(0)] = 1

    else:
        visited[s] = 1
        visit.append(s)
        dfs(p[s])
    # while not visited[s]:
    #     visited[s] = 1
    #     s = p[s]
    # if first != s:
    #     cnt += 1


t = int(input())
for tc in range(t):
    N = int(input())
    matrix = list(map(int,input().split()))
    p = [0]+matrix
    cnt = 0
    v = [0]*(N+1)
    for idx in range(1,N+1):
        if v[idx]: continue
        visited = [0]*(N+1)
        visit = [idx]
        visited[idx] = 1
        first = idx
        dfs(p[idx])
    print(cnt)