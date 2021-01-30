# 12:56 ~
from _collections import deque

def solution(board):
    def bfs(p1, p2, r, d=0): # r => 0: 가로, 1 세로
        deq = deque()
        visited = [[[0]*2 for j in range(N)] for i in range(N)]
        visited[0][0][0] = visited[0][1][0] = 1
        deq.append((p1, p2, r, d))
        while deq:
            p1, p2, r, d = deq.popleft()
            if p1 == (N-1, N-1) or p2 == (N-1,N-1):
                return d
            for dir in range(4):
                np1, np2 = (p1[0] + dy[dir], p1[1] + dx[dir]), (p2[0] + dy[dir], p2[1] + dx[dir])
                if 0 <= np1[0] < N and 0 <= np1[1] < N and 0 <= np2[0] < N and 0 <= np2[1] < N and not visited[np2[0]][np2[1]][r] and not board[np1[0]][np2[1]] and not board[np2[0]][np2[1]]:
                    visited[np2[0]][np2[1]][r] = 1
                    deq.append((np1, np2, r, d + 1))
            if r:
                LEFT, RIGHT = -1, 1
                for dir in [LEFT, RIGHT]:
                    if 0 <= p1[1]+dir < N and 0 <= p2[1] + dir < N and not board[p1[0]][p1[1] + dir] and not board[p2[0]][p2[1] + dir]:
                        if not visited[p1[0]][p1[1] + dir][1 - r]:
                            visited[p1[0]][p1[1] + dir][1 - r] = 1
                            deq.append((p1, (p1[0], p1[1] + dir), 1 - r, d + 1))
                        if not visited[p2[0]][p2[1]+dir][1 - r]:
                            visited[p2[0]][p2[1]+dir][1 - r] = 1
                            deq.append((p2, (p2[0], p2[1] + dir), 1 - r, d + 1))
            else:
                UP, DOWN = -1, 1
                for dir in [UP, DOWN]:
                    if 0 <= p1[0]+dir < N and 0 <= p2[0]+dir < N and not board[p1[0]+dir][p1[1]] and not board[p2[0]+dir][p2[1]]:
                        if not visited[p1[0]+dir][p1[1]][1-r]:
                            visited[p1[0]+dir][p1[1]][1-r] = 1
                            deq.append(((p1[0]+dir,p1[1]),p1, 1 - r, d + 1))
                        if not visited[p2[0]+dir][p2[1]][1-r]:
                            visited[p2[0] + dir][p2[1]][1 - r] = 1
                            deq.append(((p2[0]+dir,p2[1]),p2, 1 - r, d + 1))
        return 0

    dy, dx, N = [-1,0,1,0], [0,1,0,-1], len(board)
    answer = bfs((0,0),(0,1), 0)
    return answer

# board	result
ex1 = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	# 7
ex2 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]] # 21
ex3 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]] # 11
ex4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]] # 33
print(solution(ex2))