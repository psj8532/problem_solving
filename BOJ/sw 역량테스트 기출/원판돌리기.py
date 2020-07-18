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
    for i in range(N):
        for j in range(M):
            nj = (j+1)%M
            if matrix[i][j] == matrix[i][nj]:
                matrix[i][j] = 0
                matrix[i][nj] = 0
    for j in range(M):
        for i in range(N-1):
            if matrix[i][j] == matrix[i+1][j]:
                matrix[i][j] = 0
                matrix[i+1][j] = 0


def calculate(cnt):
    sum = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                cnt += 1
                sum += matrix[i][j]
    avg = sum / cnt
    sum = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                if matrix[i][j] > avg:
                    sum = sum + matrix[i][j] - 1
                elif matrix[i][j] < avg:
                    sum = sum + matrix[i][j] + 1
                else:
                    sum += matrix[i][j]
    return sum


N, M, T = map(int, input().split())
direct = [1, -1]
matrix = [list(map(int, input().split())) for _ in range(N)]
# temp_matrix = [[0]*M for _ in range(N)]
rotate_data = [list(map(int, input().split())) for _ in range(T)]
for r in range(T):
    x, d, k = rotate_data[r][0], rotate_data[r][1], rotate_data[r][2]
    for num in range(1, N+1):
        if num % x == 0:
            rotate(num-1, d, k)
    # for i in range(N):
    #     for j in range(M):
    #         temp_matrix[i][j] = matrix[][]
    check()

result = calculate(0)
print(result)