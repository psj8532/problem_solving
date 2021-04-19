import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
if len(cards) == 1:
    if cards[0] == 1: print(0)
    else: print(cards[0])
else:
    answer = 0
    heapq.heapify(cards)
    while cards:
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        sum_val = card1 + card2
        answer += sum_val
        if len(cards): heapq.heappush(cards, sum_val)

    print(answer)