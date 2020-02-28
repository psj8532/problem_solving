#11724 #14:41
import sys
sys.stdin = open("연결요소의갯수.text")

def nextfind(start):
    for next in range(n+1):
        if matrix[start][next] and not visited[next]:
            return next

def dfs(here):
    stack.append(here)
    visited[here]=True
    # result.append(here)

    while stack:
        next = nextfind(here)
        while next:
            stack.append(next)
            visited[next]=True
            # result.append(next)
            next=nextfind(next)
        here=stack.pop()
        if not stack and nextfind(here):
            stack.append(here)

n,m = map(int,input().split())
matrix=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
stack=[]
# result=[]
isEnd=False
cnt=0
for _ in range(m):
    data_y, data_x = map(int,input().split())
    matrix[data_y][data_x] = 1
    matrix[data_x][data_y] = 1
for i in range(n+1):
    for j in range(n+1):
        if matrix[i][j]:
            dfs(i)
            cnt+=1
            isEnd=True
            break
    if isEnd:
        break
for idx in range(1, n+1):
    if visited[idx]==False:
        for x in range(n+1):
            if matrix[idx][x]:
                dfs(idx)
                cnt+=1
                break
for i in range(n,0,-1):
    if visited[i]==False:
        cnt+=1
print(cnt)
#15:40