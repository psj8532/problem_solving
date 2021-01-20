# 10:25 ~
from _collections import deque
import heapq

def solution(jobs):
    answer = 0
    waiting = deque(sorted(jobs))
    curr_time, done, cand = 0, 0, []
    while done < len(jobs):
        if cand:
            time, start = heapq.heappop(cand)
            curr_time += time
            answer += curr_time - start
        else:
            start, time = waiting.popleft()
            curr_time = start + time
            answer += time
        done += 1
        while waiting and waiting[0][0] <= curr_time:
            heapq.heappush(cand, waiting.popleft()[::-1])
    return answer // len(jobs)

ex1 = [[0, 3], [1, 9], [2, 6]]  # 9
print(solution(ex1))