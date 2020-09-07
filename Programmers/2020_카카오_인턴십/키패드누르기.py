from collections import deque


def bfs(y, x, ey, ex):
    if y == ey and x == ex: return 0
    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    deq = deque()
    deq.append([y, x, 0])
    visited = [[False] * 3 for _ in range(4)]
    visited[3][0] = True
    visited[3][2] = True
    while deq:
        here = deq.popleft()
        y, x, d = here[0], here[1], here[2]
        for dir in range(4):
            ny, nx = y + direct[dir][0], x + direct[dir][1]
            if 0 <= ny < 4 and 0 <= nx < 3 and not visited[ny][nx]:
                if ny == ey and nx == ex:
                    return d + 1
                deq.append([ny, nx, d + 1])
                visited[ny][nx] = True


def solution(numbers, hand):
    answer = ''
    left_hand = [3, 0]
    right_hand = [3, 2]
    hand_position = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            left_hand = [hand_position[num][0], hand_position[num][1]]
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right_hand = [hand_position[num][0], hand_position[num][1]]
            answer += 'R'
        else:
            l_d = bfs(left_hand[0], left_hand[1], hand_position[num][0], hand_position[num][1])
            r_d = bfs(right_hand[0], right_hand[1], hand_position[num][0], hand_position[num][1])
            if l_d < r_d:
                answer += 'L'
                left_hand = [hand_position[num][0], hand_position[num][1]]
            elif l_d > r_d:
                answer += 'R'
                right_hand = [hand_position[num][0], hand_position[num][1]]
            else:
                if hand == "left":
                    left_hand = [hand_position[num][0], hand_position[num][1]]
                    answer += 'L'
                else:
                    right_hand = [hand_position[num][0], hand_position[num][1]]
                    answer += 'R'
    return answer