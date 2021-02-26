# y,x 각각의 최대,최솟값 구하기
# 구한 값을 이용해 가장 작은 직사각형의 넓이 구하기
direction = {
    0: [-1,0],
    1: [0,1],
    2: [1,0],
    3: [0,-1]
}
dy, dx = [-1,0,1,0], [0,1,0,-1]
Y, X, D = 0, 1, 2
T = int(input())
for tc in range(T):
    commands = list(input())
    curr = [0, 0, 0]
    my, My, mx, Mx = 0, 0, 0, 0
    for command in commands:
        y, x, d = curr[Y], curr[X], curr[D]
        if command == "L":
            if d: d -= 1
            else: d = 3
        elif command == "R":
            if d == 3: d = 0
            else: d += 1
        elif command == "B":
            nd = (d+2) % 4
            y, x = y + direction[nd][Y], x + direction[nd][X]
        else:
            y, x = y + direction[d][Y], x + direction[d][X]
        my, My, mx, Mx = min(my, y), max(My, y), min(mx, x), max(Mx, x)
        curr = [y, x, d]
    diff_y, diff_x = abs(My - my), abs(Mx - mx)
    print(diff_y * diff_x)