#1260 #13:57
import sys
sys.stdin = open("DFS와BFS.text","r")
#DFS에 관한 함수 정의(Stack 이용)
#BFS에 관한 함수 정의(Queue 이용)
#n:정점의 갯수, m:간선의 갯수, v:탐색을 시작할 정점의 번호

def nextFind(h):
    for next in range(1,n+1):
        if matrix[h][next] and not visited[next]:
            return next
# def nextFind(h):
#     for next in range(n,0,-1):
#         if matrix[h][next] and not visited[next]:
#             stack.append(next)


def bfs(here):
    queue=[]
    queue.append(here)
    result.append(here)
    visited[here]=1

    while queue:
        here = queue.pop(0)
        for next in range(1, n+1):
            if matrix[here][next] and not visited[next]:
                queue.append(next)
                result.append(next)
                visited[next]=1

    print(*result)

def dfs(here): #길이 없어 돌아올때 중간지점에서 pop하면 그 지점이 스택에서 사라져서 다시 돌아올때 다른경로를 탐색못함
    stack=[]
    stack.append(here)
    visited[here]=1
    result.append(here)
    while stack:
        next = nextFind(here)
        while next:
            stack.append(next)
            result.append(next)
            visited[next]=1
            next = nextFind(next)
        here=stack.pop()
        if nextFind(here):
            stack.append(here)

    print(*result)
# def dfs(here):
#     visited[here]=1
#     result.append(here)
#     nextFind(here)
#
#     while stack:
#         here = stack.pop()
#         if not visited[here]:
#             visited[here]=1
#             result.append(here)
#             nextFind(here)
#         elif stack:
#             here=stack.pop()
#
#     print(*result)
n,m,v=map(int,input().split())
data=[]
visited=[0]*(n+1)
matrix = [[0]*(n+1) for _ in range(n+1)]
result=[]
stack=[]
for _ in range(m):
    data.append(list(map(int,input().split())))

for i in range(m):
    start,end = data[i][0],data[i][1]
    matrix[start][end]=1
    matrix[end][start]=1

dfs(v)
visited=[0]*(n+1)
result=[]
bfs(v)

#17:15