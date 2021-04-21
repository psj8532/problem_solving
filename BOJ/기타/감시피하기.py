from itertools import combinations

def check_hallway():
    discovered_students = 0
    visited = [[False] * N for _ in range(N)]
    for teacher in teachers:
        ty, tx = teacher[Y], teacher[X]
        for dy, dx in direct:
            dir = 1
            ny, nx = ty + dir * dy, tx + dir * dx
            while 0 <= ny < N and 0 <= nx < N and not obstacles[ny][nx]:
                if hallway[ny][nx] == 'S' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    discovered_students += 1
                dir += 1
                ny, nx = ty + dir * dy, tx + dir * dx
    return discovered_students

answer = 'NO'
direct = [(-1,0), (0,1), (1,0), (0,-1)]
OBSTACLE, Y, X = 3, 0, 1
N = int(input())
hallway = [list(input().split()) for _ in range(N)]
candidates = []
teachers = []
for i in range(N):
    for j in range(N):
        if hallway[i][j] == 'T':
            teachers.append([i,j])
        if hallway[i][j] == 'X':
            candidates.append([i,j])

candidates_size = len(candidates)
comb = list(map(list, combinations(range(candidates_size), OBSTACLE)))
for c in comb:
    obstacles = [[False] * N for _ in range(N)]
    for idx in c:
        y, x = candidates[idx][Y], candidates[idx][X]
        obstacles[y][x] = True
    discovered = check_hallway()
    if not discovered:
        answer = 'YES'
        break
print(answer)