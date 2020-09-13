# 11:57 ~ 12:56
def dfs(m,cnt):
    direct = [(-1,0),(0,1),(1,0),(0,-1)]
    dir = [
        [2,1,0,3],
        [3,2,1,0],
        [0,3,2,1],
        [1,0,3,2]
    ]
    stack = []
    stack.append((0,0,2))
    while stack:
        y,x,fd = stack.pop()
        cnt += 1
        if y == len(m)-1 and x == len(m)-1:
            return cnt
        for i in range(4):
            ny,nx = y+direct[dir[fd][i]][0],x+direct[dir[fd][i]][1]
            if 0 <= ny < len(m) and 0 <= nx < len(m) and not m[ny][nx]:
                stack.append((ny,nx,dir[fd][i]))


def solution(maze):
    answer = -1
    answer = dfs(maze,answer)
    return answer

ex1 = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
ex2 = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
ex3 = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
ex4 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]
print(solution(ex4))