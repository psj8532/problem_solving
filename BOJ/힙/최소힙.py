import sys
sys.stdin = open("최소힙.txt", "r")
import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if not num:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)