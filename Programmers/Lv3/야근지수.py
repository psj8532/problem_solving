# 처음에 아이디어는 제대로 생각했으나 최대힙 구현을 잘못생각해서 시간복잡도 계산이 틀림햐
import heapq

def solution(works, n):
    answer = 0
    for idx, w in enumerate(works):
        works[idx] *= -1
    heapq.heapify(works)
    cnt = 0
    while cnt < n and works[0]:
        w = heapq.heappop(works)
        heapq.heappush(works, w+1)
        cnt += 1
    for idx, w in enumerate(works):
        answer += (-w) ** 2
    return answer

# works	n	result
ex1 = ([4, 3, 3],	4)	#12
ex2 = ([2, 1, 2],	1)	#6
ex3 = ([1,1],	3)	#0
print(solution(*ex1))
print(solution(*ex2))
print(solution(*ex3))