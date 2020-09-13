# 10:17 ~ 11:02
from _collections import deque


def check(temp,new_ball,answer):
    for j in range(len(temp)):
        if new_ball[0] == temp[j]:
            answer.append(new_ball.popleft())
            temp.pop(j)
            check(temp,new_ball,answer)
            return
        elif new_ball[len(new_ball) - 1] == temp[j]:
            answer.append(new_ball.pop())
            temp.pop(j)
            check(temp, new_ball, answer)
            return

def solution(ball, order):
    answer = []
    temp = []
    new_ball = deque()
    for i in range(len(ball)):
        new_ball.append(ball[i])
    for i in range(len(order)):
        # 보류 공 체크
        check(temp,new_ball,answer)
        # 볼 확인
        if new_ball[0] == order[i]:
            answer.append(new_ball.popleft())
            check(temp,new_ball,answer)
        elif new_ball[len(new_ball)-1] == order[i]:
            answer.append(new_ball.pop())
            check(temp, new_ball, answer)
        else:
            temp.append(order[i])
    return answer

ex1 = ([1, 2, 3, 4, 5, 6],[6, 2, 5, 1, 4, 3])
ex2 = ([11, 2, 9, 13, 24],[9, 2, 13, 24, 11])
print(solution(*ex2))