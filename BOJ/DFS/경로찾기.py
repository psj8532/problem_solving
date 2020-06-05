#matrix에 경로 정보 받음
#i에서 j까지의 경로(반대의 경우는 생각안해도됨
#이중 for문으로 그 자리에 있는 i(=start)와 j(=stop) 값을 받아와서 경로 있는지 탐색

def Dfs(start,end):
    global cnt
    cnt+=1
    visited[start] = 1
    if cnt==1:
        visited[start]=0

    if start == end and cnt!=1:
        global ans
        ans = 1
        return

    for next in range(n):
        if matrix[start][next] and not visited[next]:
            Dfs(next,end)
            if ans:
                return
    return

n=int(input())
matrix=[]
data = [[0]*n for _ in range(n)]
cnt=0
for _ in range(n):
    matrix.append(list(map(int,input().split())))

for y in range(n):
    for x in range(n):
        visited = [0] * n
        ans = 0
        cnt=0
        Dfs(y,x)
        data[y][x]=ans

for row in data:
    print(*row)