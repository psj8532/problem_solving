# DFS와 BFS

> 구현 방법

- DFS
  - stack을 이용
    - 그 지점에서 갈 수 있는 후보 지점들을 모두 stack에 넣음
    - 스택에 있는 후보를 꺼내면서 그 지점이 전에 방문됬던 적이 있는지 visited를 통해 확인
    - 방문하지 않았으면 그 지점으로 이동하여 다음 후보군들을 스택에 집어 넣음

- BFS
  - 큐 리스트 이용
    - 그 지점에서 갈 수 있는 지점을 큐에 넣고 바로 방문 표시
    - 큐에서 후보를 꺼낼때는 먼저 넣은 후보를 꺼내야하기 때문에 queue[0]에서 꺼내옴



> 발견한 사실

- DFS
  - stack이용 시 deque보다 리스트를 쓰는 것이 더 빨랐음
  - stack에서 갈 수 있는 점을 찾을때마다 깊이 파고 들어가는 것 보다 갈 수 있는 후보군을 넣은 다음 꺼낼때 유망한 후보들만 깊이 파고 들어가는 것이 코드가 더 깔끔했음



> 개선 사항

- BFS
  - 큐를 리스트로 만들고 pop(0)로 꺼냈는데 이렇게 하면 리스트의 크기가 클때 모든 인덱스를 하나씩 앞당겨야 하므로 시간이 오래걸림
  - 따라서, deque을 이용하여 구현하면 시간을 단축할 수 있음



> 코드

```python
from _collections import deque

def bfs(here):
    queue=[]
    queue.append(here)
    visited[here]=1
    print(here, end=' ')
    while queue:
        here = queue.pop(0)
        for next in range(1, n+1):
            if matrix[here][next] and not visited[next]:
                queue.append(next)
                print(next, end=' ')
                visited[next]=1

def dfs(here):
    stack = deque()
    stack.append(here)

    while stack:
        here = stack.pop()
        if not visited[here]:
            visited[here] = 1
            print(here, end=' ')
        else:
            continue
        for next in range(n,0,-1):
            if matrix[here][next] and not visited[next]:
                stack.append(next)
    print()

n,m,v=map(int,input().split())
data=[]
visited=[0]*(n+1)
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    data.append(list(map(int,input().split())))

for i in range(m):
    start,end = data[i][0],data[i][1]
    matrix[start][end]=1
    matrix[end][start]=1

dfs(v)
visited=[0]*(n+1)
bfs(v)
```

