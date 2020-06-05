from collections import deque

def bfs(c,p,depth):
    deq=deque()
    deq.append([c,depth])
    visited[c]=1
    while deq:
        c,depth = deq.popleft()
        if c==p:
            return depth
        for next in range(1,n+1):
            if matrix[c][next] and not visited[next]:
                deq.append([next,depth+1])
                visited[next]=1

n=int(input())
ans=list(map(int,input().split()))
m=int(input())
matrix=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    data_p,data_c=map(int,input().split())
    matrix[data_c][data_p]=1
    matrix[data_p][data_c]=1
visited=[0]*(n+1)
result=bfs(ans[0],ans[1],0)
if not result:
    result=-1
print(result)