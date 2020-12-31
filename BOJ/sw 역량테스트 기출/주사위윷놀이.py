def play(turn, val):
    global answer
    if turn == 10:
        answer = max(val, answer)
    else:
        for idx in range(4):
            ox, nx, move = horse[idx], horse[idx], dice[turn]
            if nx == 5 or nx == 10 or nx == 15:
                nx = p[nx]
                move -= 1
            if nx + move <= 21:
                nx += move
            else:
                for _ in range(move):
                    nx = p[nx]
            if v[nx] and nx != 21:
                continue
            v[ox], v[nx], horse[idx] = False, True, nx
            play(turn+1, val+values[nx])
            v[ox], v[nx], horse[idx] = True, False, ox


dice = list(map(int,input().split()))
p = [i+1 for i in range(33)]
horse = [0] * 4
v = [False] * 33
p[5], p[10], p[15] = 22, 25, 27
p[21] = 21
p[22],p[23],p[24] = 23, 24, 30
p[25], p[26] = 26, 30햐
p[32] = 20
values = [i*2 for i in range(33)]
values[0] = values[21] = 0
values[22],values[23],values[24] = 13, 16, 19
values[25],values[26] = 22, 24
values[27], values[28], values[29] = 28, 27, 26
values[30], values[31], values[32] = 25, 30, 35
answer = 0

play(0,0)
print(answer)