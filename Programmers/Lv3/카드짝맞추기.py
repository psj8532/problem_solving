# 10:45 ~ 12:28 # 틀림(구현 실패)
def solution(board, r, c):
    def move_row(start, end):
        sy, sx, ey, ex = start[0], start[1], end[0], end[1]
        cy, cx = sy, sx
        cnt = 1
        while cy != ey:
            if cy > ey: cy -= 1
            else: cy += 1
            if board[cy][cx] and not visit[board[cy][cx]]: cnt += 1
        cnt += 1
        while cx != ex:
            if cx > ex: cx -= 1
            else: cx += 1
            if board[cy][cx] and not visit[board[cy][cx]]: cnt += 1
        return cnt

    def move_col(start, end):
        sy, sx, ey, ex = start[0], start[1], end[0], end[1]
        cy, cx = sy, sx
        cnt = 1
        while cx != ex:
            if cx > ex:
                cx -= 1
            else:
                cx += 1
            if board[cy][cx] and not visit[board[cy][cx]]: cnt += 1
        cnt += 1
        while cy != ey:
            if cy > ey:
                cy -= 1
            else:
                cy += 1
            if board[cy][cx] and not visit[board[cy][cx]]: cnt += 1
        return cnt

    def find_card(curr, start, end):
        t1 = move_row(curr, start)
        t2 = move_col(curr, start)
        cnt1 = min(t1,t2)
        t1 = move_row(curr, end)
        t2 = move_col(curr, end)
        cnt2 = min(t1, t2)
        if cnt1 < cnt2:
            return curr, start, cnt1
        else:
            return curr, end, cnt2

    answer, cards = 9876543210, {}
    for i in range(4):
        for j in range(4):
            if not board[i][j]: continue
            if board[i][j] in cards:
                cards[board[i][j]].append((i,j))
            else:
                cards[board[i][j]] = [(i,j)]

    N = len(cards)
    for card in range(1,N+1):
        dist = 0
        cur = (r, c)
        # visited = [[0]*4 for _ in range(4)]
        visit = [0] * (N+1)
        print('start: ', card)
        for cd in range(1,N+1):
            # if visited[cards[cd][0][0]][cards[cd][0][1]]: continue
            if cd == card: continue
            print(cd)
            # (r,c)에서 더 가까운 쪽을 start, 먼 쪽을 end로 잡아야함
            start, end = cards[cd][0], cards[cd][1]
            s, e, d = find_card(cur, start, end)
            dist += d
            d1 = move_row(s,e)
            d2 = move_col(s,e)
            dist += min(d1,d2)
            visit[cd] =  1
            cur = e
        print()
        # print(dist)
        answer = min(dist, answer)

    return answer

# board	r	c	result
ex1 = ([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0)	# 14
ex2 = ([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],	0,	1)	# 16
print(solution(*ex1))
print(solution(*ex2))