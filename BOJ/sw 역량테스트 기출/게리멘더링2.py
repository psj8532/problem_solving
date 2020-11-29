# dy = [-1,0,1,0]
# dx = [0,1,0,-1]
N = int(input())
matrix = [[0] * (N + 1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
answer = 9876543210
# 전체 인구수 확인
total = 0
for y in range(1,N+1):
    for x in range(1,N+1):
        total += matrix[y][x]

# 범위 정하기
for y in range(2,N): # 열
    for x in range(1,N-1): # 행
        for d1 in range(1,N-1):
            for d2 in range(1,N-1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    # print('행, 열: ', x, y)
                    # print('d1, d2: ', d1, d2)
                    # print('1: ',x,y)
                    # print('2: ',x,y)
                    # print('3: ',x+d1,y-d1)
                    # print('4: ',x+d2,y+d2)
                    # t = [[0] * (N+1) for _ in range(N+1)]
                    ward = [0] * 5  # 선거구
                    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
                    for r in range(1, x + d1):
                        for c in range(1, y + 1):
                            if r+c < x+y:
                                ward[0] += matrix[r][c]
                                # t[r][c] = 1
                    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
                    for r in range(1, x + d2 + 1):
                        for c in range(y + 1,N + 1):
                            if c - r > y - x:
                                ward[1] += matrix[r][c]
                                # t[r][c] = 2
                    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
                    for r in range(x + d1, N+1):
                        for c in range(1, y-d1+d2):
                            if c - r < (y-d1) - (x+d1):
                                ward[2] += matrix[r][c]
                                # t[r][c] = 3
                    # # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
                    for r in range(x + d2 + 1, N + 1):
                        for c in range(y - d1 + d2, N + 1):
                            if r + c > (x+d2) + (y+d2):
                                ward[3] += matrix[r][c]
                                # t[r][c] = 4
                    ward[4] = total - sum(ward)
                    diff = max(ward) - min(ward)
                    # for row in t:
                    #     print(*row)
                    # print('선거구 수: ',ward)
                    # print('차이: ',diff)
                    # print('---------')
                    if diff < answer:
                        answer = diff

print(answer)