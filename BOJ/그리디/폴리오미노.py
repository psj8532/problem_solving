def solution(board):
    poliomino = ['AAAA', 'BB']
    x_cnt = 0
    candidate = []
    for ch in board:
        if ch == 'X': x_cnt += 1
        else:
            if x_cnt:
                if x_cnt & 1: return -1
                candidate.append(x_cnt)
                x_cnt = 0
            candidate.append('.')
    else:
        if x_cnt & 1: return -1
        elif x_cnt: candidate.append(x_cnt)

    answer = ''

    for cnt in candidate:
        if cnt == '.': answer += cnt
        else:
            answer += poliomino[0] * (cnt // 4)
            answer += poliomino[1] * ((cnt % 4) // 2)

    return answer

print(solution(list(input())))