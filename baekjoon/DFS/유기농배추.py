#(가로, 세로, 배추위치를 담은 k줄)
#배추위치를 담은 정보를 data리스트에 저장
#data에 담겨있는 정보를 matrix에 표현
#배추위치 탐색
    #for문으로 data리스트 담긴 위치 탐색
    #도착한 지역은 -1로 바꾸고 다음 지역 탐색
#이동할때 재귀이용

def Detect(Y,X): #
    for dir in range(len(dy)):
        new_y = Y+dy[dir]
        new_x = X+dx[dir]
        if 0<=new_y<n and 0<=new_x<m and matrix[new_y][new_x]:
            return new_y,new_x
    else:
        return -10,-10
def Dfs(y,x):
    matrix[y][x]=0
    stack.append([y,x])

    while stack:
        y,x = Detect(y,x)
        while y!=-10:
            matrix[y][x]=0
            stack.append([y,x])
            y,x = Detect(y,x)
        y,x=stack.pop()

        if stack and Detect(y,x)!=(-10,-10):
            stack.append([y,x])
        elif not stack and Detect(y,x)!=(-10,-10):
            stack.append([y,x])
    return

t = int(input())
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for tc in range(1,t+1):
    m,n,k=map(int,input().split())
    data=[]
    matrix = [[0]*m for _ in range(n)]
    cnt = 0
    stack = []
    for _ in range(k):
        data.append(list(map(int,input().split())))

    for i in range(k):
        x=data[i][0]
        y=data[i][1]
        matrix[y][x]=1

    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                Dfs(i,j)
                cnt+=1
    print(cnt)