# 10:20 ~ 15:01
from _collections import deque

def solution(board):
    def bfs():
        while deq:
            y, x, cost, d = deq.popleft()
            if (y, x) == (N - 1, N - 1):
                continue
            for dir in range(4):
                if d == dir:
                    cand = (y + dy[dir], x + dx[dir], cost + 100, d)
                else:
                    cand = (y + dy[dir], x + dx[dir], cost + 600, dir)
                if 0 <= cand[Y] < N and 0 <= cand[X] < N and not board[cand[Y]][cand[X]]:
                    if (cand[Y],cand[X]) in dist and cand[COST] > dist[(cand[Y],cand[X])]: continue
                    deq.append(cand)
                    dist[(cand[Y],cand[X])] = cand[COST]

    answer, N = 9876543210, len(board)
    dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
    U, D, R, L = 0, 1, 2, 3
    Y, X, COST, DIRECTION = 0, 1, 2, 3
    # dist = {(i,j):float('inf') for i in range(N) for j in range(N)}
    dist = {(0,0): 0}
    deq = deque()
    if not board[1][0]:
        deq.append([1, 0, 100, 1])
        dist[(1,0)] = 100
    if not board[0][1]:
        deq.append([0, 1, 100, 2])
        dist[(0, 1)] = 100
    bfs()
    return dist[(N-1,N-1)]


# board	result
ex1 = [[0,0,0],[0,0,0],[0,0,0]]	# 900
ex2 = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	# 3800
ex3 = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	# 2100
ex4 = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	# 3200
ex5 = [
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]
ex6 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0]
    ]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
print(solution(ex4))
print(solution(ex6))