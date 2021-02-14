# 18:48 ~ 20:29
H, W = map(int,input().split())
heights = list(map(int,input().split()))
matrix = [[0] * W for _ in range(H+1)]
visited = [[0] * W for _ in range(H+1)]
answer = 0
for x in range(W):
    for i in range(heights[x]):
        y = H - i
        matrix[y][x] = 1

for y in range(H,0,-1):
    for x in range(1,W-1):
        if matrix[y][x] or visited[y][x]: continue
        if matrix[y][x-1] and matrix[y][x+1]:
            answer += 1
            visited[y][x] = 1
        elif matrix[y][x-1] and not matrix[y][x+1]:
            for nx in range(x+1, W-1):
                if matrix[y][nx+1]:
                    for j in range(nx,x-1,-1):
                        visited[y][j] = 1
                        answer += 1
                    break
print(answer)