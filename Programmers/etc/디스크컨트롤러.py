# 10:25 ~
import heapq

def solution(jobs):
    def get_min(k,tt,ett):
        nonlocal min_v, min_idx
        if k == len(cand):
            if ett < min_v:
                min_v = ett
                min_idx = visit[0]

            return
        for i in range(len(cand)):
            if not visited[i]:
                visited[i] = 1
                visit.append(i)
                s,e = cand[i]
                total = (tt-s) + e
                get_min(k+1,tt+e,ett + total)
                visit.pop()
                visited[i] = 0
        return
    answer = 0
    cnt = len(jobs)
    heapq.heapify(jobs)
    t = 0
    while jobs:
        cand = []
        while jobs:
            s,e = heapq.heappop(jobs)
            if s <= t:
                cand.append([s,e])
            elif not cand and t <= s:
                cand.append([s,e])
            elif not cand and t < s:
                break
            else:
                heapq.heappush(jobs, [s,e])
                break

        min_v = 9876543210
        min_idx = -1
        visit = []
        visited = [0] * len(cand)
        get_min(0,t,answer)
        for i in range(len(cand)):
            if i == min_idx: continue
            heapq.heappush(jobs, cand[i])
        answer += (t-cand[min_idx][0]) + cand[min_idx][1]
        t += cand[min_idx][1]
        # print('총합시간: ', answer, '완료시간: ', t)
    return answer // cnt


ex1 = [[0, 3], [1, 9], [2, 6]]  # 9
print(solution(ex1))