import sys
sys.stdin = open("촌수계산.text","r")
from _collections import deque

def bfs(pa,ch,depth):
    deq=deque()
    deq.append([pa,depth])
    visited[pa]=1
    while deq:
        here = deq.popleft()
        pa,depth=here[0],here[1]
        if pa==ch:
            global result
            result=depth
            return
        for next in range(1,n+1):
            if 0<=next<n+1 and matrix[pa][next] and not visited[next]:
                visited[next]=1
                deq.append([next,depth+1])

n=int(input())
ans=list(map(int,input().split()))
m=int(input())
visited=[0]*(n+1)
matrix=[[0]*(n+1) for _ in range(n+1)]
result=-1
for i in range(m):
    data=list(map(int,input().split()))
    parent,child=data[0],data[1]
    matrix[parent][child]=1

bfs(ans[0],ans[1],0)
if result==-1:
    visited = [0] * (n + 1)
    bfs(ans[1],ans[1],0)

print(result)