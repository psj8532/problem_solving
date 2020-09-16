# 22:36 ~ 23:13
from collections import deque


def solution(food_times, k):
    answer = 0
    food = deque()
    for i in range(len(food_times)):
        food.append([food_times[i],i+1])
    t = 0
    while food:
        h,idx = food.popleft()
        if t == k:
            answer = idx
            break
        elif h > 1:
            food.append([h-1,idx])
        t += 1

    if answer == 0:
        answer = -1
    return answer

ex1 = [3, 1, 2],5
print(solution(*ex1))