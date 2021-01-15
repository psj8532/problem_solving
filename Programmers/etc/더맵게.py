import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        val = a + b * 2
        heapq.heappush(scoville, val)
        answer += 1
    return answer

# scoville	K	return
ex1 = ([1, 2, 3, 9, 10, 12], 7)	# 2
ex2 = ([1,2], 3)
print(solution(*ex2))