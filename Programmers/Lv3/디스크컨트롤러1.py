from _collections import deque
import heapq

def solution(jobs):
    waiting, cand, jobs_size = deque(sorted(jobs)), [], len(jobs)
    curr_time = total = done = 0

    while done < jobs_size:
        if cand:
            time, input_time = heapq.heappop(cand)
            curr_time += time
            total += curr_time - input_time
        else:
            input_time, time = waiting.popleft()
            total += time
            curr_time = input_time + time
        done += 1
        while waiting and waiting[0][0] <= curr_time:
            heapq.heappush(cand, waiting.popleft()[::-1])
    return total // jobs_size