def permutation(index):
    if index == K:
        temp = a[:]
        perm.append(temp)
        return
    else:
        in_perm = [False]*K
        for i in range(index):
            in_perm[a[i]] = True
        c = [0]*K
        cnt = 0
        for i in range(K):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[index] = c[i]
            permutation(index+1)

def count():
    global min
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += matrix[i][j]
            if sum > min:
                break
        if sum < min:
            min = sum

def copy(o,n):
    for i in range(N):
        for j in range(M):
            n[i][j] = o[i][j]
    return n

direct = [(0,1),(1,0),(0,-1),(-1,0)]
N,M,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
rotation = [list(map(int,input().split())) for _ in range(K)]
temp_matrix = [[0]*M for _ in range(N)]
perm = []
a = [0]*K
permutation(0)
min = 9876543210
temp_matrix = copy(matrix,temp_matrix)
for idx in range(len(perm)):
    for i in range(K):
        r,c,s = rotation[perm[idx][i]][0]-1,rotation[perm[idx][i]][1]-1,rotation[perm[idx][i]][2]
        visited = [[False]*M for _ in range(N)]
        for j in range(1,s+1):
            dir = 0
            y,x = r-j,c-j
            ny,nx = y+direct[dir][0],x+direct[dir][1]
            temp1 = matrix[y][x]
            while not visited[ny][nx]:
                temp2 = matrix[ny][nx]
                matrix[ny][nx] = temp1
                temp1 = temp2
                y,x = ny,nx
                visited[y][x] = 1
                if (y,x) == (r-j,c-j) or (y,x) == (r-j,c+j) or (y,x) == (r+j,c-j) or (y,x) == (r+j,c+j):
                    dir = (dir+1)%4
                ny,nx = y+direct[dir][0],x+direct[dir][1]
    count()
    matrix = copy(temp_matrix,matrix)
print(min)