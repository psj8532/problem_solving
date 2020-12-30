# 13:50 ~ 14:14 / # 15:05 ~ 16:28

def play(turn, val):
    global answer
    if turn == 10:
        print('val: ', val, 'answer: ', answer)
        if val > answer:
            answer = val
    else:
        # 말 선택
        for idx, lst in enumerate(horse):
            here, b = lst
            branch = b
            if horse_visit[idx]:
                continue
            if branch == 0:
                here_idx = board[branch].index(here)
                t = here_idx + dice[turn]
                print('t: ',t,'board[branch][t]: ',board[branch][t], 'val: ',val)
                print(*horse)
                # print('branch: ', branch, 'here_idx: ', here_idx)
                next = board[branch][t]
                if t >= len(board[branch]):
                    horse_visit[idx] = True
                    break
                if next == 10:
                    branch = 1
                    here_idx = 0
                elif next == 20:
                    branch = 2
                    here_idx = 0
                elif next == 30:
                    branch = 3
                    here_idx = 0
            else:
                here_idx = board[branch].index(here)
                t = here_idx + dice[turn]
                # 도착 지점에 도달
                if branch == 4 and t >= len(board[branch]):
                    # 말 제거
                    horse_visit[idx] = True
                    break
                if t >= len(board[branch]):
                    t %= len(board[branch])
                    branch = 4
                print('t: ', t, 'board[branch][t]: ', board[branch][t], 'val: ', val)
                print(*horse)

                next = board[branch][t]
            print(*horse_visit)
            # 목표 지점에 다른 말이 있는지 확인
            next_idx = board[branch].index(next)
            if next != -1 and board_visit[branch][next_idx]:
                continue
            horse[idx][0],horse[idx][1] = next,branch
            if next == -1:
                board_visit[branch][here_idx] = False
                play(turn+1, val)
                board_visit[branch][here_idx] = True
            else:
                board_visit[branch][here_idx] = False
                board_visit[branch][next_idx] = True
                play(turn + 1, val+next)
                board_visit[branch][here_idx] = True
                board_visit[branch][next_idx] = False
            horse[idx][0],horse[idx][1] = here,b
            horse_visit[idx] = False

dice = list(map(int,input().split()))
board = [
    [i for i in range(0,41,2)],
    [10, 13, 16, 19],
    [20, 22, 24],
    [30, 28, 27, 26],
    [25, 30, 35, 40],
]
horse = [[0] * 2 for _ in range(4)]
horse_visit = [False] * 4
board_visit = []
for i in range(5):
    temp = [False] * len(board[i])
    board_visit.append(temp)
answer = 0
play(0, 0)
print(answer)
