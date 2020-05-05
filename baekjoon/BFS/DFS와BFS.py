#1260 #13:57
import sys
sys.stdin = open("DFS와BFS.text","r")
from _collections import deque
#DFS에 관한 함수 정의(Stack 이용)
#BFS에 관한 함수 정의(Queue 이용)
#n:정점의 갯수, m:간선의 갯수, v:탐색을 시작할 정점의 번호
#이 문제는 stack을 이용할 때 덱보다 리스트를 사용하는 것이 시간이 더 빠름
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

#17:15