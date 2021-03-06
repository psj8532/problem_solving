def rotate(i, dir, count):
    for cnt in range(count):
        temp_pull = matrix[i][0]
        nj = 0
        for j in range(M):
            nj = (nj+direct[dir]) % M
            temp_keep = matrix[i][nj]
            matrix[i][nj] = temp_pull
            temp_pull = temp_keep


def check():
    isSame = False
    for i in range(N):
        for j in range(M):
            nj = (j+1)%M
            if matrix[i][j] and (matrix[i][j] == matrix[i][nj]):
                isSame = True
                temp_matrix[i][j] = -1
                temp_matrix[i][nj] = -1

    for j in range(M):
        for i in range(N-1):
            if matrix[i][j] and matrix[i][j] == matrix[i+1][j]:
                isSame = True
                temp_matrix[i][j] = -1
                temp_matrix[i+1][j] = -1

    for i in range(N):
        for j in range(M):
            if temp_matrix[i][j] == -1:
                matrix[i][j] = 0
                temp_matrix[i][j] = -1
    if isSame:
        return True
    else:
        return False


def calculate(cnt):
    sum = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                cnt += 1
                sum += matrix[i][j]
    if not cnt:
        return
    avg = sum / cnt
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                if matrix[i][j] > avg:
                    matrix[i][j] -= 1
                elif matrix[i][j] < avg:
                    matrix[i][j] += 1


N, M, T = map(int, input().split())
direct = [1, -1]
matrix = [list(map(int, input().split())) for _ in range(N)]
rotate_data = [list(map(int, input().split())) for _ in range(T)]
for t in range(T):
    x, d, k = rotate_data[t][0], rotate_data[t][1], rotate_data[t][2]
    for num in range(1, N+1):
        if num % x == 0:
            rotate(num-1, d, k)
    temp_matrix = [[0] * M for _ in range(N)]
    if not check():
        calculate(0)
result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            result += matrix[i][j]
print(result)