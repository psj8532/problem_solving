import copy

def play(r,c,sd,answer,fish,matrix):
    global ans
    # 물고기 이동
    for n, lst in fish.items():
        if not visited[n]:
            y, x, d = lst
            nd = d
            isFirst = True
            while isFirst or nd != d:
                isFirst = False
                ny, nx = y + direct[nd][0], x + direct[nd][1]
                if 0 <= ny < 4 and 0 <= nx < 4 and matrix[ny][nx] != -1:
                    if matrix[ny][nx] == 0:  # 비어있을 때
                        matrix[ny][nx] = n
                        fish[n][0], fish[n][1], fish[n][2] = ny, nx, nd
                        matrix[y][x] = 0
                    else:  # 다른 물고기가 있을 때
                        o = matrix[ny][nx]
                        fish[n][0], fish[o][0] = fish[o][0], fish[n][0]
                        fish[n][1], fish[o][1] = fish[o][1], fish[n][1]
                        fish[n][2] = nd
                        matrix[ny][nx] = matrix[y][x]
                        matrix[y][x] = o
                    break
                nd = (nd + 1) % 8

    # 상어 이동
    isFail = True
    for i in range(3):
        ny, nx = r + direct[sd][0] + direct[sd][0]*i, c + direct[sd][1]+direct[sd][1]*i
        if 0 <= ny < 4 and 0 <= nx < 4 and matrix[ny][nx] > 0:
            isFail = False
            t_matrix = copy.deepcopy(matrix)
            matrix[r][c] = 0
            n = matrix[ny][nx]
            visited[n] = True  # 잡아 먹힌 물고기
            matrix[ny][nx] = -1
            t_fish = copy.deepcopy(fish)
            play(ny,nx,fish[n][2],answer+n,fish,matrix)

            fish = copy.deepcopy(t_fish)
            matrix = copy.deepcopy(t_matrix)
            visited[n] = False  # 잡아 먹힌 물고기

    if isFail:
        if answer > ans:
            ans = answer


lst = [list(map(int,input().split())) for _ in range(4)]
fish = {i:[] for i in range(17)} # 물고기 번호별 좌표,방향 정보
visited = [False]*17
matrix = [[0]*4 for _ in range(4)] # 물고기 번호
direct = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
for i in range(4):
    for j in range(4):
        number,D = lst[i][2*j],lst[i][2*j+1]
        matrix[i][j] = number
        fish[number].append(i)
        fish[number].append(j)
        fish[number].append(D-1)

visited[0] = True
ans = 0
first_fish = matrix[0][0]
matrix[0][0] = -1
visited[first_fish] = True
play(0,0,fish[first_fish][2],first_fish,fish,matrix)

print(ans)