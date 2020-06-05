#2206 #9:20
from _collections import deque

def bfs(y, x, depth,cnt):
    deq = deque()
    deq.append([y, x, depth, cnt])

    while deq:
        here = deq.popleft()
        y, x, depth, cnt = here[0], here[1], here[2], here[3]

        if (y, x) == (r - 1, c - 1):
            return depth
        for dir in range(len(dy)):
            new_y = y + dy[dir]
            new_x = x + dx[dir]
            if 0 <= new_y < r and 0 <= new_x < c and not visited[cnt][new_y][new_x] and matrix[new_y][new_x] and cnt:
                deq.append([new_y, new_x, depth + 1,cnt-1])
                visited[cnt-1][new_y][new_x] = 1
            elif 0 <= new_y < r and 0 <= new_x < c and not visited[cnt][new_y][new_x] and not matrix[new_y][new_x]:
                deq.append([new_y, new_x, depth + 1,cnt])
                visited[cnt][new_y][new_x] = 1

r, c = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(r)]
visited = [[[0] * c for _ in range(r)] for _ in range(2)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dep=bfs(0, 0, 1, 1)
if dep:
    print(dep)
else:
    print(-1)
# 더 탐색해도 의미없는 곳은 최대한 가지 말아야한다!!
#19:16