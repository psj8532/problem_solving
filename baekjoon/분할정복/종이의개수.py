def check(y,x,k):
    for i in range(y,y+k):
        for j in range(x,x+k):
            if paper[y][x] != paper[i][j]:
                return False
    return True

def div(sy,sx,n):
    m = n//3
    if check(sy,sx,n):
        result[paper[sy][sx]+1] += 1
    else:
        for i in range(3):
            for j in range(3):
                div(sy+m*i, sx+m*j, m)

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
result = [0]*3
div(0,0,N)
for val in result:
    print(val)