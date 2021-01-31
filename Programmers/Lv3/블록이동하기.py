# 12:56 ~
from _collections import deque

def solution(board):
    def bfs(p1, p2, r): # r => 0: 가로, 1 세로
        cand = []
        for dir in range(4):
            np1, np2 = (p1[0] + dy[dir], p1[1] + dx[dir]), (p2[0] + dy[dir], p2[1] + dx[dir])
            if not new_board[np1[0]][np1[1]] and not new_board[np2[0]][np2[1]]:
                cand.append((np1, np2, r))
        if r:
            LEFT, RIGHT = -1, 1
            for dir in [LEFT, RIGHT]:
                if not new_board[p1[0]][p1[1] + dir] and not new_board[p2[0]][p2[1] + dir]:
                    cand.append((*sorted([(p1[0], p1[1] + dir), p1]), 1 - r))
                    cand.append((*sorted([(p2[0], p2[1] + dir), p2]), 1 - r))
        else:
            UP, DOWN = -1, 1
            for dir in [UP, DOWN]:
                if not new_board[p1[0] + dir][p1[1]] and not new_board[p2[0] + dir][p2[1]]:
                    cand.append((*sorted([p1, (p1[0]+dir, p1[1])]), 1 - r))
                    cand.append((*sorted([p2, (p2[0]+dir, p2[1])]), 1 - r))
        return cand
    dy, dx, N = [-1,0,1,0], [0,1,0,-1], len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    deq = deque()
    deq.append(((1,1), (1,2), 0, 0))
    visit = set(((1,1), (1,2), 0, 0))
    while deq:
        p1, p2, rot, depth = deq.popleft()
        if p1 == (N, N) or p2 == (N,N):
            return depth
        for tp in bfs(p1, p2, rot):
            if tp not in visit:
                deq.append((*tp, depth + 1))
                visit.add(tp)


# board	result
ex1 = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	# 7
ex2 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]] # 21
ex3 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]] # 11
ex4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]] # 33
print(solution(ex4))