def solution(n, build_frame):
    def check_p(y,x):
        if y == n-1 or pillar[y+1][x]: return True
        elif x and beam[y][x - 1]: return True
        elif beam[y][x]: return True
        return False

    def check_b(y,x):
        if pillar[y + 1][x] or pillar[y + 1][x + 1]:
            return True
        elif x and beam[y][x - 1] and beam[y][x + 1]:
            return True
        return False

    def check_delete():
        for i in range(n):
            for j in range(n):
                if pillar[i][j] and not check_p(i,j):
                    return False
                if beam[i][j] and not check_b(i,j):
                    return False
        return True

    n += 1
    answer, N = [], len(build_frame)
    pillar = [[0]*n for _ in range(n)]
    beam = [[0]*n for _ in range(n)]

    for x, y, kinds, command in build_frame:
        # kinds 0: 기둥 1: 보 # com 0: 삭제 1: 설치
        y = n - 1 - y
        if kinds and command:
            if check_b(y, x):
                beam[y][x] = 1
        elif kinds and not command:
            beam[y][x] = 0
            if not check_delete():
                beam[y][x] = 1
        elif not kinds and command:
            if check_p(y ,x):
                pillar[y][x] = 1
        else:
            pillar[y][x] = 0
            if not check_delete():
                pillar[y][x] = 1

    for i in range(n):
        for j in range(n):
            ni = n - 1 - i
            if pillar[i][j]:
                answer.append([j,ni,0])
            if beam[i][j]:
                answer.append([j,ni,1])
    answer.sort()
    return answer

ex1 = (5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
ex2 = (5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
print(solution(*ex2))