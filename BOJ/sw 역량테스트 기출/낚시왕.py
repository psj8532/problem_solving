def copy():
    for i in range(R):
        for j in range(C):
            if [temp_matrix[i][j][0], temp_matrix[i][j][1], temp_matrix[i][j][2]] != [0,0,0]:
                shark_matrix[i][j][0], shark_matrix[i][j][1], shark_matrix[i][j][2] = temp_matrix[i][j][0], temp_matrix[i][j][1], temp_matrix[i][j][2]
                temp_matrix[i][j][0], temp_matrix[i][j][1], temp_matrix[i][j][2] = 0, 0, 0

def catch(x):
    size = 0
    for y in range(R):
        s, d, z = shark_matrix[y][x][0], shark_matrix[y][x][1], shark_matrix[y][x][2]
        if [s,d,z] != [0,0,0]:
            size = z
            shark_matrix[y][x][0], shark_matrix[y][x][1], shark_matrix[y][x][2] = 0, 0, 0
            break
    return size

def move(y,x,v,dir,size):
    cnt = 0
    while cnt < v:
        ny = y + direct[dir][0]
        nx = x + direct[dir][1]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            dir += 2
            dir %= 4
            ny = y + direct[dir][0]
            nx = x + direct[dir][1]
        y,x = ny,nx
        cnt += 1
    s,d,z = temp_matrix[y][x][0], temp_matrix[y][x][1], temp_matrix[y][x][2]
    if [s,d,z] == [0,0,0]:
        temp_matrix[y][x][0], temp_matrix[y][x][1], temp_matrix[y][x][2] = v, dir, size
    else:
        if size > z:
            temp_matrix[y][x][0], temp_matrix[y][x][1], temp_matrix[y][x][2] = v, dir, size

R,C,M = map(int,input().split())
direct = [(-1,0),(0,1),(1,0),(0,-1)]
shark_matrix = [[[0]*3 for i in range(C)] for j in range(R)]
sum = 0

for i in range(M):
    r,c,s,d,z = map(int,input().split())
    if d == 1: d = 0
    elif d == 3: d = 1
    elif d == 4: d = 3
    shark_matrix[r-1][c-1][0], shark_matrix[r-1][c-1][1], shark_matrix[r-1][c-1][2] = s, d, z

for here in range(C):
    temp_matrix = [[[0] * 3 for i in range(C)] for j in range(R)]
    sum += catch(here)
    for i in range(R):
        for j in range(C):
            s, d, z = shark_matrix[i][j][0], shark_matrix[i][j][1], shark_matrix[i][j][2]
            if [s,d,z] != [0,0,0]:
                move(i,j,s,d,z)
                shark_matrix[i][j][0], shark_matrix[i][j][1], shark_matrix[i][j][2] = 0, 0, 0
    copy()

print(sum)