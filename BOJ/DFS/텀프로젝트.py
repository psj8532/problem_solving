import sys
import time
sys.stdin = open("텀프로젝트.txt", "r")
stime = time.time()

# def dfs(s):
#     global cnt
#     if memo[s]:
#         cnt += 1
#         for x in range(len(visit)):
#             memo[visit.pop()] = 1
#         # memo[first] = 1
#         return
#     if visited[s]:
#         if first != s:
#             cnt += 1
#         else:
#             for x in range(len(visit)):
#                 memo[visit.pop()] = 1
#
#     else:
#         visited[s] = 1
#         visit.append(s)
#         dfs(p[s])
def dfs(s):
    global cnt
    if visited[s]:
        if memo[s]:
            if first == s:
                for x in range(len(visit)):
                    here = visit.pop()
                    cycle[here] = 1
                    memo[here] = 1
                return
            cnt += 1
            for x in range(len(visit)):
                here = visit.pop()
                memo[here] = 1
        else:
            if first != s:
                cnt += 1
                for x in range(len(visit)):
                    here = visit.pop()
                    memo[here] = 1
            else:
                for x in range(len(visit)):
                    here = visit.pop()
                    cycle[here] = 1
                    memo[here] = 1
    else:
        visited[s] = 1
        visit.append(s)
        dfs(p[s])


t = int(input())
for tc in range(t):
    N = int(input())
    matrix = list(map(int,input().split()))
    p = [0]+matrix
    cnt = 0
    memo = [0]*(N+1)
    visited = [0]*(N+1)
    cycle = [0]*(N+1)
    for idx in range(1,N+1):
        if cycle[idx]: continue
        visit = [idx]
        visited[idx] = 1
        first = idx
        dfs(p[idx])
    print(cnt)

print(time.time()-stime)