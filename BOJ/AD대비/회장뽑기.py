from _collections import deque


def bfs(h):
    while deq:
        h = deq.popleft()
        s,d = h[0],h[1]
        for n in adj[s]:
            if not visited[n]:
                deq.append((n,d+1))
                visited[n] = True
    return d


N = int(input())
adj = {i:[] for i in range(N+1)}
while 1:
    s,e = map(int,input().split())
    if s == -1 and e == -1:
        break
    adj[s].append(e)
    adj[e].append(s)
arr = []
min = 9876543210
for i in range(1,N+1):
    deq = deque()
    visited = [0]*(N+1)
    deq.append((i,0))
    visited[i] = True
    grade = bfs(i)
    if grade < min:
        arr = [i]
        cnt = 1
        min = grade
    elif grade == min:
        arr.append(i)
        cnt += 1
print(min,cnt)
if cnt == 1:
    print(arr[0])
else:
    arr.sort()
    print(*arr)