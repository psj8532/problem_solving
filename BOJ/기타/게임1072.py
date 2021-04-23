import math

def solution(total, win, pov):
    answer = max_game = 10000000000
    left, right = 1, max_game

    while left <= right:
        mid = (left + right) // 2
        curr_pov = math.floor((win + mid) * 100 // (total + mid))
        if curr_pov == pov:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer

total_game, win_game = map(int,input().split())
pov = math.floor(win_game * 100 // total_game)
if pov >= 99:
    print(-1)
else:
    print(solution(total_game, win_game, pov))