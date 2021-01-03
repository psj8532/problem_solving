#17:23 ~
import math
def solution(progresses, speeds):
    answer = []
    lst = []
    for i in range(len(progresses)):
        cur, speed = progresses[i], speeds[i]
        remainder = 100 - cur
        t = math.ceil(remainder / speed)
        lst.append([cur,t])
    while lst:
        p,time = lst.pop(0)
        cnt = 1
        temp = []
        for i in range(len(lst)):
            if lst[i][1] <= time:
                cnt += 1
                temp.append(i)
            else:
                break
        for i in range(len(temp)-1,-1,-1):
            lst.pop(temp[i])
        answer.append(cnt)
    return answer


# progresses	speeds	return
ex1 = [[93, 30, 55], [1, 30, 5]] # [2, 1]
ex2 = [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]] # [1, 3, 2]
print(solution(*ex1))