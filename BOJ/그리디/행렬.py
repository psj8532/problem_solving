N, M = map(int,input().split())
A = [list(map(int,input())) for _ in range(N)]
B = [list(map(int,input())) for _ in range(N)]
answer = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] == B[i][j]: continue
        answer += 1
        for y in range(i, i+3):
            for x in range(j, j+3):
                A[y][x] = 1 - A[y][x]

isDiff = False
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            isDiff = True
            break
    if isDiff: break
if isDiff: print(-1)
else: print(answer)
