def spring():
    for location, trees in live_trees.items():
        y, x = location[Y], location[X]
        for index, age in enumerate(trees):
            if field[y][x] >= age:
                field[y][x] -= age
                live_trees[location][index] = age + 1
            else:
                live = trees[:index]
                dead = trees[index:]
                live_trees[location] = live
                dead_trees[location] = dead
                break
    return

def summer(field, dead_trees):
    for location, trees in dead_trees.items():
        if not trees: continue
        y, x = location[Y], location[X]
        for age in trees:
            field[y][x] += age // 2
        dead_trees[location] = []
    return field, dead_trees

def fall(live_trees):
    def breed(y, x, live_trees):
        for dir in range(D):
            ny, nx = y + direct[dir][Y], x + direct[dir][X]
            if 0 <= ny < N and 0 <= nx < N:
                live_trees[(ny, nx)].append(1)

        return live_trees

    for location, trees in live_trees.items():
        if not trees: continue
        for age in trees:
            if age % 5: continue
            live_trees = breed(location[Y], location[X], live_trees)

    for location, trees in live_trees.items():
        if not trees: continue
        live_trees[location] = sorted(trees)
    return live_trees

def winter(field):
    for i in range(N):
        for j in range(N):
            field[i][j] += food[i][j]
    return field

def check_life_and_death(live_trees):
    cnt = 0
    for trees in live_trees.values():
        cnt += len(trees)
    return cnt

Y, X, D = 0, 1, 8
N, M, K = map(int,input().split())
food = [list(map(int,input().split())) for _ in range(N)]
treeData = [list(map(int,input().split())) for _ in range(M)]
field = [[5] * N for _ in range(N)]
live_trees = {(i,j): [] for i in range(N) for j in range(N)}
dead_trees = {(i,j): [] for i in range(N) for j in range(N)}
direct = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
year = 0

for y,x,z in treeData:
    live_trees[(y-1,x-1)].append(z)

for location in live_trees:
    live_trees[location] = sorted(live_trees[location])

while year < K:
    spring()
    field, dead_trees = summer(field, dead_trees)
    live_trees = fall(live_trees)
    field = winter(field)
    year += 1

answer = check_life_and_death(live_trees)
print(answer)