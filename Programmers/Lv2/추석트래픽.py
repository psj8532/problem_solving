from _collections import deque

def solution(lines):
    def change_time(end):
        t = list(end.split(':'))
        hour = int(t[0]) * 3600
        minute = int(t[1]) * 60
        sec = float(t[2])
        return hour + minute + sec

    deq = deque()
    answer = 0

    for info in lines:
        _, S, T = info.split()
        end = change_time(S)
        start = round(end - float(T[:-1]) + 0.001, 3)
        deq.append([start, end])

    while deq:
        s, e = deq.popleft()
        cnt = 1
        for comp_s, comp_e in deq:
            if comp_s < e + 1:
                cnt += 1
        answer = max(cnt, answer)

    return answer

ex1 = [
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
ex2 = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
ex3 = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(ex3))