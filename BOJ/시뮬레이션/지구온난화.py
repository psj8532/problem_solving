# 11:55 ~ 12:43
dy, dx = [-1,0,1,0], [0,1,0,-1]
R, C = map(int,input().split())
matrix = [['.'] * (C+2)]
for _ in range(R):
    lst = list(input())
    matrix.append(['.'] + lst + ['.'])
else:
    matrix.append(['.'] * (C+2))
sea = {}
for i in range(1,R+1):
    for j in range(1,C+1):
        sea[(i,j)] = 0
        for dir in range(4):
            ni, nj = i + dy[dir], j + dx[dir]
            if matrix[i][j] == 'X' and matrix[ni][nj] == '.':
                sea[(i,j)] += 1

for position, cnt in sea.items():
    if cnt >= 3:
        matrix[position[0]][position[1]] = '.'

sy,sx,ey,ex = 0,C+1,R+1,0
for i in range(1,R+1):
    for j in range(1,C+1):
        if matrix[i][j] == 'X' and not sy:
            sy = i
            break
    if sy: break

for i in range(R,0,-1):
    for j in range(C,0,-1):
        if matrix[i][j] == 'X' and ey == R+1:
            ey = i
            break
    if ey != R+1: break

for i in range(1,R+1):
    for j in range(1,C+1):
        if matrix[i][j] == 'X':
            if j < sx: sx = j
            continue

for i in range(R,0,-1):
    for j in range(C,0,-1):
        if matrix[i][j] == 'X':
            if j > ex: ex = j
            continue

for i in range(sy,ey+1):
    for j in range(sx,ex+1):
        print(matrix[i][j], end='')
    print()
