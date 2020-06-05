import sys
sys.stdin = open("색종이붙이기.txt", "r")

def recover():
    temp = visited.pop()
    for idx in range(len(temp)):
        matrix[temp[idx][0]][temp[idx][1]] = 1

def check(y,x,n):
    a = []
    if 0<=y+n-1<10 and 0<=x+n-1<10:
        for r in range(y,y+n):
            for c in range(x,x+n):
                if not matrix[r][c]:
                    return False
                a.append((r, c))
        temp = a[:]
        for idx in range(len(temp)):
            matrix[temp[idx][0]][temp[idx][1]] = 0
        visited.append(temp)
        return True
    else:
        return False

def dfs(cnt):
    global min
    for i in range(10):
        for j in range(10):
            for k in range(1,6):
                if paper[k] and matrix[i][j] and check(i,j,k):
                    paper[k] -= 1
                    dfs(cnt+1)
                    paper[k] += 1
                    recover()
    for i in range(10):
        for j in range(10):
            if matrix[i][j]:
                return
    if cnt < min:
        min = cnt

matrix = [list(map(int,input().split())) for _ in range(10)]
visited = []
paper= [0,5,5,5,5,5]
min = 9876543210
dfs(0)
if min < 9876543210:
    print(min)
else:
    print(-1)