import sys
sys.stdin = open("최대힙.txt", "r")
import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    elif num > 0:
        heapq.heappush(heap,(-num, num))