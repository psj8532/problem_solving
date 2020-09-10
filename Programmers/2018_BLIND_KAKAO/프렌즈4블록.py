# 2020.09.10.21:50 ~ 22:40
from _collections import deque


def solution(m, n, board):
    answer = 0
    matrix = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = board[i][j]
    flag = False
    while 1:
        flag = False
        visited = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j] and matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j+1]:
                    visited[i][j] = visited[i+1][j] = visited[i][j+1] = visited[i+1][j+1] = 1
                    flag = True
        if not flag: break
        #remove
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    matrix[i][j] = 0
                    answer += 1
        # pull
        for j in range(n):
            posi = deque()
            for i in range(m-1,-1,-1):
                if not matrix[i][j]:
                    posi.append((i,j))
                elif posi and matrix[i][j]:
                    r,c = posi.popleft()
                    matrix[r][c] = matrix[i][j]
                    matrix[i][j] = 0
                    posi.append((i,j))

    return answer

# ex1 = 4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
# ex2 = 6,6,['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
# ex3 = 6, 6, ['AAAAAA', 'BBAATB', 'BBAATB', 'BBAATB', 'JJJTAA', 'JJJTAA']
# print(solution(*ex3))