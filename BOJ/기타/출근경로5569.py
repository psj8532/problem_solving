def dfs(y, x, dir, turn):
    global answer

    if (y, x) == (destination[Y], destination[X]):
        answer += 1
        return

    if turn:
        for nd in direction:
            ny, nx = y + direction[nd][Y], x + direction[nd][X]
            if 0 <= ny and nx < W:
                if nd != dir and dir:
                    dfs(ny, nx, nd, False)
                else:
                    dfs(ny, nx, nd, True)
    else:
        ny, nx = y + direction[dir][Y], x + direction[dir][X]
        if 0 <= ny and nx < W:
            dfs(ny, nx, dir, True)

Y, X = 0, 1
direction = {
    'UP': [-1, 0],
    'RIGHT': [0, 1],
}
W, H = map(int,input().split())
destination = [0, W - 1]
start = [H - 1, 0]
answer = 0
dfs(start[Y], start[X], '', True)
print(answer)